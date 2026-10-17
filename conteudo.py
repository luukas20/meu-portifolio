# CONTEÚDO DA PÁGINA
# Fonte única dos textos, tags, imagens e links da homepage. O template só percorre estas listas.
# Imagens: caminho dentro de public/static/images/ (WebP gerados por tools/otimizar_imagens.py). Descrições dos projetos aceitam HTML (renderizadas com |safe).
# Projeto com "link": None não tem imagem clicável.
# "chave_bot": trecho que precisa existir em prompts/conhecimento.md (conferido por tests/test_conteudo.py).
# O conhecimento do chatbot fica em prompts/conhecimento.md (editado à mão): ao mudar algo aqui, conferir lá também.


def tag(icone, nome):
    return {"icone": icone, "nome": nome}


ESPECIALIDADES = [
    {

        "titulo": "Data Science",
        "descricao": "Aplicando algoritmos de Machine Learning para solucionar desafios complexos e impulsionar a eficiência operacional.",
        "tags": [
            tag("icones/estatistica.webp", "Estatística"),
            tag("icones/python.webp", "Python"),
            tag("icones/r.webp", "R/RStudio"),
        ],
    },
    {

        "titulo": "Business Intelligence",
        "descricao": "Capacitando líderes com dashboards interativos e relatórios inteligentes para uma tomada de decisão baseada em dados.",
        "tags": [
            tag("icones/estatistica.webp", "Estatística"),
            tag("icones/python.webp", "Python"),
            tag("icones/power-bi.webp", "Power BI"),
            tag("icones/sql.webp", "SQL"),
        ],
    },
    {

        "titulo": "Risco de Crédito",
        "descricao": "Desenvolvendo e validando modelos de score de crédito que garantem uma concessão de crédito mais segura e eficiente. Em conformidade com a CMN 4966/21.",
        "tags": [
            tag("icones/estatistica.webp", "Estatística"),
            tag("icones/python.webp", "Python"),
            tag("icones/r.webp", "R/RStudio"),
        ],
    },
]

SOBRE_MIM = [
    "Profissional apaixonado por Ciência de Dados e Machine Learning, com uma formação em Estatística pela Universidade Federal de Sergipe. Atualmente, atuo como Analista de Transformação na Iguá Saneamento, onde aplico minha expertise em Data Science e Business Intelligence para otimizar a tomada de decisões estratégicas.",
    "Minha trajetória é marcada por um profundo interesse em técnicas de Machine Learning, utilizando as linguagens R e Python para desenvolver soluções inovadoras. Além disso, possuo um sólido domínio em SQL Server, Power BI e DAX, ferramentas que me permitem transformar dados complexos em insights acionáveis e visualizações impactantes.",
    "Acredito que a combinação de estatística, programação e visualização é essencial para revelar insights valiosos a partir dos dados. Estou sempre em busca de aprimorar minhas habilidades técnicas e criativas, desafiando-me a alcançar novos patamares de excelência.",
]

REDES = [
    {"nome": "LinkedIn", "url": "https://www.linkedin.com/in/luukas20/"},
    {"nome": "GitHub", "url": "https://github.com/luukas20"},
    {"nome": "E-mail", "url": "mailto:lucas.estatistico@outlook.com"},
]

# Currículo em PDF (arquivo dentro de public/static/). O Word de origem fica fora do repositório.
CURRICULO = {
    "arquivo": "docs/Curriculo-Lucas-Costa.pdf",
    "nome_download": "Currículo Lucas Costa.pdf",
}

PROJETOS = [
    {
        "titulo": "Modelagem de Perda Esperada (PE)",
        "tags": [
            tag("icones/python.webp", "Python"),
            tag("icones/estatistica.webp", "Data Science"),
            tag("icones/servicos-financeiros.webp", "Risco de Crédito"),
        ],
        "imagem": "projetos/perda-esperada.webp",
        "chave_bot": "Modelagem de Perda Esperada (PE)",
        "link": None,
        "descricao": "Desenvolvi uma solução robusta para a estimativa da Perda Esperada em portfólios de cartão de crédito através da fórmula <math class='formula' display='block'><mi>PE</mi><mo>=</mo><mi>PD</mi><mo>×</mo><mi>LGD</mi><mo>×</mo><mi>EAD</mi></math> <strong>• Probabilidade de Default (PD)</strong>; <br> <strong>• Loss Given Default (LGD)</strong>; <br> <strong>• Exposure at Default (EAD)</strong>. <br> Com essa abordagem de <i>Machine Learning</i>, alcancei um <strong>Índice de Cobertura de 115%</strong>. Garantindo uma gestão de limites precisa e maior resiliência financeira para a carteira.",
    },
    {
        "titulo": "Visão Computacional (Gatos vs. Cachorros)",
        "tags": [
            tag("icones/python.webp", "Python"),
            tag("icones/estatistica.webp", "Data Science"),
            tag("icones/rede-neural.webp", "Rede CNN"),
        ],
        "imagem": "projetos/cat-vs-dog.webp",
        "chave_bot": "Gatos vs. Cachorros",
        "link": "https://github.com/luukas20/cnn-cat-vs-dog",
        "descricao": "Neste projeto, explorei a classificação de imagens usando Redes Neurais Convolucionais (CNNs). Inicialmente, treinei uma CNN customizada do zero, que alcançou uma acurácia sólida de +85%. Em seguida, utilizei <em>Transfer Learning</em> com a arquitetura <strong>ResNet50</strong> (pré-treinado pela Microsoft), atingindo impressionantes 98% de acurácia!",
    },
    {
        "titulo": "Faturamento vs Meta",
        "tags": [
            tag("icones/power-bi.webp", "Power BI"),
            tag("icones/microsoft.webp", "Power Automate"),
            tag("icones/sql.webp", "SQL"),
        ],
        "imagem": "projetos/faturamento-vs-meta.webp",
        "chave_bot": "performance comercial",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNDM5YTczNTUtNzkxYS00MzZjLTlkZmYtNjZmMDBhYWU4MTg0IiwidCI6ImE3YmJlZjdmLTY1NzctNDA3Mi05YzhkLTk1ZDNmMWVmMWM1ZSJ9",
        "descricao": "Acompanhando a performance comercial em tempo real! Este painel compara o faturamento realizado com as metas estabelecidas, trazendo insights sobre evolução mensal, desempenho por produto e ranking de vendedores. Além disso, destaca ticket médio, notas emitidas e projeções de forecast para o fechamento anual.",
    },
    {
        "titulo": "Previsão BOVA11",
        "tags": [
            tag("icones/power-bi.webp", "Power BI"),
            tag("icones/python.webp", "Python"),
            tag("icones/garch.webp", "ARMA-GARCH"),
            tag("icones/rede-neural.webp", "REDE LSTM"),
        ],
        "imagem": "projetos/previsao-bova11.webp",
        "chave_bot": "BOVA11",
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNjJlN2JmZGMtMjViOS00OGNiLWFlYzMtZjIzOGI1ODhmM2ZiIiwidCI6ImE3YmJlZjdmLTY1NzctNDA3Mi05YzhkLTk1ZDNmMWVmMWM1ZSJ9",
        "descricao": "Analisando o futuro financeiro com precisão! Este painel compara o poder da inteligência artificial, representada por uma rede neural LSTM, e da estatística, através do modelo GARCH, para prever a cotação do BOVA11. Utilizamos R e Python para treinar os modelos e o Power BI para visualizar os resultados. A junção perfeita de tecnologia e análise de dados.",
    },
    {
        "titulo": "Controle de Gastos Pessoais",
        "tags": [
            tag("icones/power-bi.webp", "Power BI"),
            tag("icones/microsoft.webp", "FORMS"),
            tag("icones/microsoft.webp", "POWER AUTOMATE"),
        ],
        "imagem": "projetos/controle-de-gastos.webp",
        "chave_bot": "finanças pessoais",
        "link": None,
        "descricao": "Controlando as finanças pessoais com clareza e inteligência! Este painel acompanha a carteira ao longo do tempo, destacando receitas, despesas e a média mensal, além de detalhar a variação do saldo acumulado. Também traz insights sobre despesas por categoria, distribuição das transações e comparativos entre metas e valores realizados. Oferece uma visão completa para tomada de decisões financeiras mais conscientes e estratégicas.",
    },
    {
        "titulo": "Previsão Ações Streamlit",
        "tags": [
            tag("icones/python.webp", "Python"),
            tag("icones/streamlit.webp", "STREAMLIT"),
            tag("icones/garch.webp", "ARMA-GARCH"),
        ],
        "imagem": "projetos/previsao-acoes-streamlit.webp",
        "chave_bot": "Streamlit",
        "link": "https://lucas-estatistico-acoes.streamlit.app/",
        "descricao": "Este painel interativo, desenvolvido com Streamlit, oferece uma análise aprofundada do desempenho de qualquer ação de sua escolha. Digite o ticker desejado para explorar dados históricos, visualizar gráficos de preços e acompanhar as previsões geradas pelo modelo ARMA-GARCH. Uma ferramenta poderosa e flexível para suas análises e projeções no mercado financeiro.",
    },
]


# --- TORRE: primeira tela, trajetória e ferramentas ---------------------------------------------
# Frentes: reescritas em out/2026 com fatos do currículo e dos projetos do Lucas (nada inventado); trajetória, ferramentas,
# idiomas e cursos copiados do currículo atualizado (out/2026). Ordem da trajetória: do mais recente para a base.

TAGLINE = "Transformando dados complexos em decisões estratégicas."

CITACAO = {
    "texto": "O pensamento estatístico será um dia tão necessário para a cidadania eficiente quanto a capacidade de ler e escrever.",
    "autor": "H. G. Wells",
}

FRENTES = [
    {
        "titulo": "Estatística e Machine Learning",
        "texto": "Índice de Cobertura de 115% na perda esperada, 98% de acurácia em visão computacional e previsão de séries financeiras.",
        "itens": ["Python", "R", "PD, LGD e EAD", "ARMA-GARCH", "Redes LSTM", "CNN"],
    },
    {
        "titulo": "BI e dados",
        "texto": "Dashboards em Power BI sobre dados modelados, integrados e automatizados.",
        "itens": ["Power BI", "DAX", "SQL Server", "MySQL", "Oracle SQL", "Snowflake", "Pentaho", "Power Automate"],
    },
    {
        "titulo": "Análise para decisão",
        "texto": "Análises de CAPEX, OPEX e viabilidade de projetos que sustentam decisões rápidas e precisas.",
        "itens": ["CAPEX e OPEX", "Viabilidade de projetos", "Indicadores de inadimplência", "Metas estratégicas", "Python", "R", "IA"],
    },
]

TRAJETORIA = [
    {
        "empresa": "Iguá Saneamento",
        "cargo": "Analista de Transformação Sr.",
        "periodo": "fev/2026 – atualmente",
        "atual": True,
        "topicos": [
            "Desenvolvimento de Soluções de Data Science para Otimização de Processos",
            "Análise de Dados para Suporte à Tomada de Decisão Estratégica",
            "Análise de Dados para Viabilidade de Projetos de Transformação",
            "Análise de CAPEX e OPEX para Projetos de Transformação",
            "Desenvolvimento de Dashboards e Relatórios para Monitoramento de Indicadores de Performance dos Projetos de Transformação",
            "Gerenciamento do Power BI Service do Setor de Transformação",
        ],
    },
    {
        "empresa": "Cencosud",
        "cargo": "Analista Estratégia de Risco PL.",
        "periodo": "abr/2025 – fev/2026",
        "atual": False,
        "topicos": [
            "Adequação a CMN 4966/21",
            "Modelagem da Probability of Default - PD",
            "Modelagem da Loss Given Default - LGD",
            "Modelagem da Exposure At Default - EAD",
            "Modelagem da Provisão da Perda Esperada utilizando PD, LGD e EAD",
            "Avaliação de Modelos Credit Score de Empresas Especializadas",
            "Cálculo de Indicadores de Inadimplência",
            "Construção de Dashboard no Power BI",
            "Gerenciamento do Power BI Service",
        ],
    },
    {
        "empresa": "Cencosud",
        "cargo": "Analista Estratégia de Risco Jr.",
        "periodo": "jan/2024 – abr/2025",
        "atual": False,
        "topicos": [
            "Construção do Modelo Behaviour Score para Risco de Crédito",
            "Gerenciamento do Data Warehouse em SQL Server e MySQL",
            "Cálculo de Indicadores de Inadimplência",
            "Provisão da Perda Esperada ao Risco de Crédito",
            "Construção de Dashboard no Power BI",
            "Gerenciamento do Power BI Service",
        ],
    },
    {
        "empresa": "Hospital Primavera",
        "cargo": "Estagiário de Analista de Business Intelligence",
        "periodo": "abr/2023 – dez/2023",
        "atual": False,
        "topicos": [
            "Criação de Consultas em Oracle SQL, SQL Server, MySQL",
            "Automatização de Indicadores do Interact Direto dos Bancos de Dados",
            "Construção de Dashboard no Power BI e Gerenciamento do Power BI Service",
            "Automação de Tarefas via Power Automate",
        ],
    },
    {
        "empresa": "Tribunal Regional Eleitoral - TRE",
        "cargo": "Estagiário de Estatística",
        "periodo": "fev/2022 – mar/2023",
        "atual": False,
        "topicos": [
            "Gerenciamento dos Indicadores Estratégicos do TRE-SE",
            "Gerenciamento das Metas do CNJ",
            "Gerenciamento dos Indicadores Plano de Logística Sustentável do TRE-SE",
            "Shiny App para Apuração de Votos em Tempo Real direto da API do TSE",
        ],
    },
]

# A base da torre: a formação.
FUNDACAO = {
    "instituicao": "Universidade Federal de Sergipe - UFS",
    "curso": "Bacharelado em Estatística",
    "periodo": "2019/2024",
    "tcc": "TCC - Análise Comparativa Entre Modelos De Previsão ARMA-GARCH e Redes Neurais LSTM: Um Estudo de Caso Aplicado ao BOVA11",
}

FERRAMENTAS = ["R Core Team", "Python", "SQL Server", "Snowflake", "Power BI", "QlikView", "Pentaho Data Integration", "Excel"]

IDIOMAS = [
    {"idioma": "Português", "nivel": "Nativo"},
    {"idioma": "Inglês", "nivel": "Nível Básico"},
    {"idioma": "Espanhol", "nivel": "Nível Básico"},
]

CURSOS = [
    "Formação - Power BI - Data University Cencosud",
    "Curso - Data Warehouse Week - Xperium",
    "Curso - Data Expert: Além do Básico - Xperium",
    "Curso - Master Power BI De A à Z - Udemy",
    "Curso - Microsoft Excel 2016 Avançado - Fundação Bradesco",
    "Curso - Introdução à programação com python - Digital Innovation One Inc.",
    "Curso - SQL SERVER Criando suas primeiras consultas - Digital Innovation One Inc.",
    "Formação - Consultas com Oracle Database - Alura",
    "Curso - Análise de Dados em Linguagem R - Enap",
    "Curso - Análise de Dados como Suporte a Tomada de Decisão - Enap",
    "Curso - Construindo Aplicações Web com R Utilizando o Pacote Shiny - UFS",
    "Curso - Organização Apresentação e Tratamento de Dados Científicos - UFS",
]

NAVEGACAO = [
    ("Trajetória", "#trajetoria"),
    ("Projetos", "#portfolio"),
    ("Especialidades", "#especialidades"),
    ("Sobre", "#sobre"),
    ("Contato", "#contato"),
]
