import re
from datetime import datetime
from pathlib import Path

import conteudo
import views
from main import app

RAIZ = Path(__file__).resolve().parent.parent
PASTA_STATIC = RAIZ / "static"
PASTA_IMAGENS = PASTA_STATIC / "images"


def home():
    return app.test_client().get("/").get_data(as_text=True)


def imagens_referenciadas():
    nomes = {"lucas.webp"}
    for item in conteudo.ESPECIALIDADES + conteudo.PROJETOS:
        nomes.update(tag["icone"] for tag in item["tags"])
    nomes.update(projeto["imagem"] for projeto in conteudo.PROJETOS)
    return nomes


def test_imagens_do_conteudo_existem():
    faltando = sorted(nome for nome in imagens_referenciadas() if not (PASTA_IMAGENS / nome).is_file())
    assert faltando == []


def test_fontes_hospedadas_existem():
    css = (PASTA_STATIC / "style.css").read_text(encoding="utf-8")
    fontes = re.findall(r'url\("(fonts/[^"]+)"\)', css)
    assert fontes, "o CSS deveria carregar as fontes de static/fonts/"
    assert [f for f in fontes if not (PASTA_STATIC / f).is_file()] == []


def test_home_renderiza_todo_o_conteudo():
    html = home()
    for item in conteudo.ESPECIALIDADES + conteudo.PROJETOS:
        assert item["titulo"] in html
    for frente in conteudo.FRENTES:
        assert frente["titulo"] in html and frente["texto"] in html
    for cargo in conteudo.TRAJETORIA:
        assert cargo["empresa"] in html and cargo["cargo"] in html and cargo["periodo"] in html
        assert all(topico in html for topico in cargo["topicos"])
    for rede in conteudo.REDES:
        assert rede["url"] in html
    for paragrafo in conteudo.SOBRE_MIM:
        assert paragrafo in html
    for curso in conteudo.CURSOS:
        assert curso in html
    assert conteudo.TAGLINE in html and conteudo.CITACAO["autor"] in html


def test_cada_projeto_tem_os_campos_obrigatorios():
    for projeto in conteudo.PROJETOS:
        for campo in ("titulo", "tags", "imagem", "descricao"):
            assert projeto.get(campo), f"{projeto.get('titulo')}: falta {campo}"
        assert "link" in projeto  # None = sem link


def test_curriculo_existe_e_tem_botao_de_download():
    arquivo = PASTA_STATIC / conteudo.CURRICULO["arquivo"]
    assert arquivo.is_file()
    assert arquivo.read_bytes().startswith(b"%PDF")

    html = home()
    assert f'/static/{conteudo.CURRICULO["arquivo"]}' in html
    assert f'download="{conteudo.CURRICULO["nome_download"]}"' in html

    resposta = app.test_client().get(f'/static/{conteudo.CURRICULO["arquivo"]}')
    assert resposta.status_code == 200
    assert resposta.mimetype == "application/pdf"


def test_chatbot_conhece_idiomas_e_snowflake():
    conhecimento = (views.PASTA_PROMPTS / "conhecimento.md").read_text(encoding="utf-8")
    for termo in ("Inglês - Nível Básico", "Espanhol - Nível Básico", "Snowflake"):
        assert termo in conhecimento


def test_chatbot_conhece_todos_os_projetos_da_pagina():
    conhecimento = (views.PASTA_PROMPTS / "conhecimento.md").read_text(encoding="utf-8")
    faltando = [p["titulo"] for p in conteudo.PROJETOS if p["chave_bot"] not in conhecimento]
    assert faltando == [], f"Faltam em prompts/conhecimento.md: {faltando}"


def test_chatbot_conhece_todas_as_empresas_da_trajetoria():
    conhecimento = (views.PASTA_PROMPTS / "conhecimento.md").read_text(encoding="utf-8")
    faltando = sorted({c["empresa"] for c in conteudo.TRAJETORIA if c["empresa"] not in conhecimento})
    assert faltando == [], f"Faltam em prompts/conhecimento.md: {faltando}"


def test_projeto_sem_link_nao_tem_botao_de_abrir():
    html = home()
    com_link = [p for p in conteudo.PROJETOS if p["link"]]
    sem_link = [p for p in conteudo.PROJETOS if not p["link"]]
    assert sem_link, "o teste espera ao menos um projeto sem link"
    assert html.count("Abrir o projeto") == len(com_link)
    assert 'href="#"' not in html


def test_grafias_corrigidas_e_ano_automatico():
    html = home()
    for correto in ("Business Intelligence", "POWER AUTOMATE"):
        assert correto in html
    for errado in ("Busines Inteligence", "ATOMATE", "&copy; 2025"):
        assert errado not in html
    assert f"&copy; {datetime.now().year} " in html
    assert "portif" not in html.lower()
    assert 'id="portfolio"' in html and 'href="#portfolio"' in html


def test_pagina_sem_dependencias_externas():
    html = home()
    for externo in ("polyfill.io", "cdn.jsdelivr.net", "fonts.googleapis.com", "mathjax"):
        assert externo not in html.lower()
    assert "<script src=" in html and html.count("<script src=") == 1


def test_estrutura_acessivel_basica():
    html = home()
    assert '<html lang="pt-BR">' in html
    assert html.count("<h1") == 1
    assert 'class="pular"' in html and 'id="principal"' in html
    # toda imagem declara alt (vazio quando decorativa)
    sem_alt = [tag for tag in re.findall(r"<img\b[^>]*>", html) if " alt=" not in tag]
    assert sem_alt == []
    # nenhum botão dentro de link (HTML inválido que existia antes)
    assert not re.search(r"<a\b[^>]*>\s*<button", html)


def test_pagina_sem_emojis():
    html = home()
    emojis = re.findall("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]", html)
    assert emojis == []


def test_curriculo_so_no_menu_e_no_contato():
    html = home()
    nome = conteudo.CURRICULO["nome_download"]
    # exatamente dois botões de currículo: um no menu e outro em "Vamos conversar"
    assert html.count(f'download="{nome}"') == 2
    topo = html.split('id="topo"')[1].split('id="trajetoria"')[0]
    assert "download=" not in topo  # a primeira tela não tem botão de currículo
    assert "Ver projetos" in topo and "Falar comigo" in topo
    contato = html.split('id="contato"')[1]
    assert "Baixar currículo (PDF)" in contato


def test_cargo_atual_aparece_na_primeira_tela():
    html = home()
    topo = html.split('id="topo"')[1].split('id="trajetoria"')[0]
    atual = conteudo.TRAJETORIA[0]
    assert atual["cargo"] in topo and atual["empresa"] in topo


def test_previa_de_compartilhamento():
    html = home()
    assert 'property="og:image"' in html and "/static/images/og.jpg" in html
    assert 'name="twitter:card" content="summary_large_image"' in html
    assert (PASTA_IMAGENS / "og.jpg").is_file()


def test_ordem_e_acessibilidade_da_primeira_tela():
    html = home()
    topo = html.split('id="topo"')[1].split('id="trajetoria"')[0]
    # as frentes não são títulos de seção (só o h1 e os h2 das seções entram no índice)
    assert "<h2>" not in topo
    # cada link "Abrir o projeto" tem nome acessível próprio
    assert html.count('class="so-leitor">: ') == len([p for p in conteudo.PROJETOS if p["link"]])
