from datetime import datetime
from pathlib import Path

import conteudo
import views
from main import app

PASTA_IMAGENS = Path(__file__).resolve().parent.parent / "static" / "images"


def imagens_referenciadas():
    nomes = set()
    for item in conteudo.ESPECIALIDADES + conteudo.PROJETOS:
        nomes.update(tag["icone"] for tag in item["tags"])
        nomes.add(item.get("icone") or item["imagem"])
    nomes.update(rede["icone"] for rede in conteudo.REDES)
    return nomes


def test_imagens_do_conteudo_existem():
    faltando = sorted(nome for nome in imagens_referenciadas() if not (PASTA_IMAGENS / nome).is_file())
    assert faltando == []


def test_home_renderiza_todo_o_conteudo():
    html = app.test_client().get("/").get_data(as_text=True)
    for item in conteudo.ESPECIALIDADES + conteudo.PROJETOS:
        assert item["titulo"] in html
    for rede in conteudo.REDES:
        assert rede["url"] in html
    for paragrafo in conteudo.SOBRE_MIM:
        assert paragrafo in html


def test_cada_projeto_tem_os_campos_obrigatorios():
    for projeto in conteudo.PROJETOS:
        for campo in ("titulo", "tags", "imagem", "descricao"):
            assert projeto.get(campo), f"{projeto.get('titulo')}: falta {campo}"
        assert "link" in projeto  # None = sem link


def test_curriculo_existe_e_tem_botao_de_download():
    arquivo = PASTA_IMAGENS.parent / conteudo.CURRICULO["arquivo"]
    assert arquivo.is_file()
    assert arquivo.read_bytes().startswith(b"%PDF")

    html = app.test_client().get("/").get_data(as_text=True)
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


def test_projeto_sem_link_nao_tem_imagem_clicavel():
    html = app.test_client().get("/").get_data(as_text=True)
    sem_link = [p for p in conteudo.PROJETOS if not p["link"]]
    assert sem_link, "o teste espera ao menos um projeto sem link"
    assert html.count("card-image sem-link") == len(sem_link)
    assert 'href="#"' not in html


def test_grafias_corrigidas_e_ano_automatico():
    html = app.test_client().get("/").get_data(as_text=True)
    for correto in ("Business Intelligence", "Início", "POWER AUTOMATE"):
        assert correto in html
    for errado in ("Busines Inteligence", "Inicio<", "ATOMATE", "&copy; 2025"):
        assert errado not in html
    assert "portif" not in html.lower()
    assert 'id="portfolio"' in html and 'href="#portfolio"' in html
    assert f"&copy; {datetime.now().year} " in html
