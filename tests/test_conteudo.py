from datetime import datetime
from pathlib import Path

import conteudo
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
    assert f"&copy; {datetime.now().year} " in html
