# CONTEÚDO DA PÁGINA
# Fonte única dos textos, tags, imagens e links da homepage. O template só percorre estas listas.
# Imagens: nome do arquivo dentro de static/images/. Descrições dos projetos aceitam HTML (renderizadas com |safe).
# Projeto com "link": None não tem imagem clicável.
# "chave_bot": trecho que precisa existir em prompts/conhecimento.md (conferido por tests/test_conteudo.py).
# O conhecimento do chatbot fica em prompts/conhecimento.md (editado à mão): ao mudar algo aqui, conferir lá também.


def tag(icone, nome):
    return {"icone": icone, "nome": nome}


ESPECIALIDADES = [
    {
        "icone": "Estatistica.png",
        "titulo": "Data Science",
        "descricao": "Aplicando algoritmos de Machine Learning para solucionar desafios complexos e impulsionar a eficiência operacional.",
        "tags": [
            tag("Estatistica.png", "Estatística"),
            tag("Python.png", "Python"),
            tag("R Core Team.png", "R/RStudio"),
        ],
    },
    {
        "icone": "Business Intelligence.png",
        "titulo": "Business Intelligence",
        "descricao": "Capacitando líderes com dashboards interativos e relatórios inteligentes para uma tomada de decisão baseada em dados.",
        "tags": [
            tag("Estatistica.png", "Estatística"),
            tag("Python.png", "Python"),
            tag("Power BI.png", "Power BI"),
            tag("Data Base.png", "SQL"),
        ],
    },
    {
        "icone": "Serviços Financeiros.png",
        "titulo": "Risco de Crédito",
        "descricao": "Desenvolvendo e validando modelos de score de crédito que garantem uma concessão de crédito mais segura e eficiente. Em conformidade com a CMN 4966/21.",
        "tags": [
            tag("Estatistica.png", "Estatística"),
            tag("Python.png", "Python"),
            tag("R Core Team.png", "R/RStudio"),
        ],
    },
]

SOBRE_MIM = [
    "Profissional apaixonado por Ciência de Dados e Machine Learning, com uma formação em Estatística pela Universidade Federal de Sergipe. Atualmente, atuo como Analista de Transformação na Iguá Saneamento, onde aplico minha expertise em Data Science e Business Intelligence para otimizar a tomada de decisões estratégicas. 📊",
    "Minha trajetória é marcada por um profundo interesse em técnicas de Machine Learning, utilizando as linguagens R e Python para desenvolver soluções inovadoras. Além disso, possuo um sólido domínio em SQL Server, Power BI e DAX, ferramentas que me permitem transformar dados complexos em insights acionáveis e visualizações impactantes. 🎯",
    "Acredito que a combinação de estatística, programação e visualização é essencial para revelar insights valiosos a partir dos dados. Estou sempre em busca de aprimorar minhas habilidades técnicas e criativas, desafiando-me a alcançar novos patamares de excelência 🚀.",
]

REDES = [
    {"nome": "LinkedIn", "url": "https://www.linkedin.com/in/luukas20/", "icone": "Linkedin.png"},
    {"nome": "GitHub", "url": "https://github.com/luukas20", "icone": "GitHub.png"},
    {"nome": "E-mail", "url": "mailto:lucas.estatistico@outlook.com", "icone": "E-Mail.png"},
]

# Currículo em PDF (arquivo dentro de static/). O Word de origem fica fora do repositório.
CURRICULO = {
    "arquivo": "docs/Curriculo-Lucas-Costa.pdf",
    "nome_download": "Currículo Lucas Costa.pdf",
}

PROJETOS = [
    {
        "titulo": "📊 Modelagem de Perda Esperada (PE)",
        "tags": [
            tag("Python.png", "Python"),
            tag("Estatistica.png", "Data Science"),
            tag("Serviços Financeiros.png", "Risco de Crédito"),
        ],
        "imagem": "Perda Esperada.png",
        "chave_bot": "Modelagem de Perda Esperada (PE)",
        "link": None,
        "descricao": r"Desenvolvi uma solução robusta para a estimativa da Perda Esperada em portfólios de cartão de crédito através da fórmula $$ PE = PD \times LGD \times EAD $$ <strong>• Probabilidade de Default (PD)</strong>; <br> <strong>• Loss Given Default (LGD)</strong>; <br> <strong>• Exposure at Default (EAD)</strong>. <br> Com essa abordagem de <i>Machine Learning</i>, alcancei um <strong>Índice de Cobertura de 115%</strong> ✅. Garantindo uma gestão de limites precisa e maior resiliência financeira para a carteira. 💰📈",
    },
    {
        "titulo": "🚀 Visão Computacional (Gatos vs. Cachorros)",
        "tags": [
            tag("Python.png", "Python"),
            tag("Estatistica.png", "Data Science"),
            tag("Rede LSTM.png", "Rede CNN"),
        ],
        "imagem": "Cat vs Dog.png",
        "chave_bot": "Gatos vs. Cachorros",
        "link": "https://github.com/luukas20/cnn-cat-vs-dog",
        "descricao": "Neste projeto, explorei a classificação de imagens usando Redes Neurais Convolucionais (CNNs) 🧠. Inicialmente, treinei uma CNN customizada do zero, que alcançou uma acurácia sólida de +85% 📈. Em seguida, utilizei <em>Transfer Learning</em> ✨ com a arquitetura <strong>ResNet50</strong> (pré-treinado pela Microsoft), atingindo impressionantes 98% de acurácia! 🚀",
    },
    {
        "titulo": "Faturamento vs Meta",
        "tags": [
            tag("Power BI.png", "Power BI"),
            tag("Microsoft.png", "Power Automate"),
            tag("Data Base.png", "SQL"),
        ],
        "imagem": "Data Expert.png",
        "chave_bot": "performance comercial",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNDM5YTczNTUtNzkxYS00MzZjLTlkZmYtNjZmMDBhYWU4MTg0IiwidCI6ImE3YmJlZjdmLTY1NzctNDA3Mi05YzhkLTk1ZDNmMWVmMWM1ZSJ9",
        "descricao": "Acompanhando a performance comercial em tempo real! 📊🚀 Este painel compara o faturamento realizado com as metas estabelecidas, trazendo insights sobre evolução mensal, desempenho por produto e ranking de vendedores. Além disso, destaca ticket médio, notas emitidas e projeções de forecast para o fechamento anual. 💼✨",
    },
    {
        "titulo": "Previsão BOVA11",
        "tags": [
            tag("Power BI.png", "Power BI"),
            tag("Python.png", "Python"),
            tag("GARCH.png", "ARMA-GARCH"),
            tag("Rede LSTM.png", "REDE LSTM"),
        ],
        "imagem": "Previsão BOVA11.png",
        "chave_bot": "BOVA11",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNjJlN2JmZGMtMjViOS00OGNiLWFlYzMtZjIzOGI1ODhmM2ZiIiwidCI6ImE3YmJlZjdmLTY1NzctNDA3Mi05YzhkLTk1ZDNmMWVmMWM1ZSJ9",
        "descricao": "Analisando o futuro financeiro com precisão! 📈✨ Este painel compara o poder da inteligência artificial, representada por uma rede neural LSTM, e da estatística, através do modelo GARCH, para prever a cotação do BOVA11. Utilizamos R e Python para treinar os modelos e o Power BI para visualizar os resultados. A junção perfeita de tecnologia e análise de dados. 💹🤖",
    },
    {
        "titulo": "Controle de Gastos Pessoais",
        "tags": [
            tag("Power BI.png", "Power BI"),
            tag("Microsoft.png", "FORMS"),
            tag("Microsoft.png", "POWER AUTOMATE"),
        ],
        "imagem": "Controle de Gastos.png",
        "chave_bot": "finanças pessoais",
        "link": None,
        "descricao": "Controlando as finanças pessoais com clareza e inteligência! 💰📊 Este painel acompanha a carteira ao longo do tempo, destacando receitas, despesas e a média mensal, além de detalhar a variação do saldo acumulado. Também traz insights sobre despesas por categoria, distribuição das transações e comparativos entre metas e valores realizados. Oferece uma visão completa para tomada de decisões financeiras mais conscientes e estratégicas. 📉✨",
    },
    {
        "titulo": "Previsão Ações Streamlit",
        "tags": [
            tag("Python.png", "Python"),
            tag("Dev Streamlit.png", "STREAMLIT"),
            tag("GARCH.png", "ARMA-GARCH"),
        ],
        "imagem": "Dashboard Streamlit.png",
        "chave_bot": "Streamlit",
        "link": "https://lucas-estatistico-acoes.streamlit.app/",
        "descricao": "📈✨ Este painel interativo, desenvolvido com Streamlit, oferece uma análise aprofundada do desempenho de qualquer ação de sua escolha. Digite o ticker desejado para explorar dados históricos, visualizar gráficos de preços e acompanhar as previsões geradas pelo modelo ARMA-GARCH. Uma ferramenta poderosa e flexível para suas análises e projeções no mercado financeiro. 💹💻",
    },
]
