"""Gera as imagens leves usadas pelo site a partir dos originais em imagens-originais/.

Uso (na raiz do projeto, com o venv ativo):
    python tools/otimizar_imagens.py

- Capturas dos projetos  -> public/static/images/projetos/<nome>.webp (900 px de largura)
- Ícones das etiquetas   -> public/static/images/icones/<nome>.webp  (64 px)
- Foto                   -> public/static/images/<nome>.webp         (720 px de largura)
Os originais ficam fora da pasta servida (imagens-originais/) e nunca vão para a página.
"""
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGINAIS = RAIZ / "imagens-originais"
SAIDA = RAIZ / "public" / "static" / "images"

# nome do original -> nome final (sem acento, sem espaço)
PROJETOS = {
    "Perda Esperada.png": "perda-esperada",
    "Cat vs Dog.png": "cat-vs-dog",
    "Data Expert.png": "faturamento-vs-meta",
    "Previsão BOVA11.png": "previsao-bova11",
    "Controle de Gastos.png": "controle-de-gastos",
    "Dashboard Streamlit.png": "previsao-acoes-streamlit",
}
ICONES = {
    "Estatistica.png": "estatistica",
    "Python.png": "python",
    "R Core Team.png": "r",
    "Power BI.png": "power-bi",
    "Data Base.png": "sql",
    "Serviços Financeiros.png": "servicos-financeiros",
    "Microsoft.png": "microsoft",
    "Rede LSTM.png": "rede-neural",
    "GARCH.png": "garch",
    "Dev Streamlit.png": "streamlit",
}
FOTOS = {"Foto Perfil.jpeg": "lucas"}


COR_ICONE = (11, 122, 117)  # --acento (verde-azulado)


def salvar(origem, destino, largura, qualidade, recolorir=False):
    destino.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(origem) as img:
        img = img.convert("RGBA") if img.mode in ("RGBA", "LA", "P") else img.convert("RGB")
        if recolorir:
            # os ícones são desenhos de uma cor só: mantém o contorno (alfa) e troca a cor
            alfa = img.getchannel("A")
            img = Image.new("RGBA", img.size, COR_ICONE + (0,))
            img.putalpha(alfa)
        if img.width > largura:
            altura = round(img.height * largura / img.width)
            img = img.resize((largura, altura), Image.LANCZOS)
        img.save(destino, "WEBP", quality=qualidade, method=6)
    return destino.stat().st_size


def main():
    total = 0
    for pasta, tabela, largura, qualidade in (
        ("projetos", PROJETOS, 900, 72),
        ("icones", ICONES, 64, 90),
        (".", FOTOS, 720, 80),
    ):
        for original, nome in tabela.items():
            origem = ORIGINAIS / original
            if not origem.is_file():
                print(f"  (pulado, não achei) {original}")
                continue
            destino = SAIDA / pasta / f"{nome}.webp"
            tamanho = salvar(origem, destino, largura, qualidade, recolorir=(pasta == "icones"))
            total += tamanho
            print(f"{tamanho / 1024:7.1f} KB  {destino.relative_to(RAIZ)}")
    print(f"total: {total / 1024:.0f} KB")


if __name__ == "__main__":
    main()
