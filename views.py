from main import app
from flask import render_template, request, jsonify
from dotenv import load_dotenv
import os
from google import genai

# Rotas
@app.route('/', endpoint='pagina_home')
def homepage():
    return render_template("homepage.html")

# 1. CONFIGURAÇÃO INICIAL
load_dotenv() # Carrega as variáveis do arquivo .env

# 2. CONFIGURAÇÃO DA API DO GEMINI
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Define os dados do LinkedIn
dados_linkedin = """
## RESUMO PROFISSIONAL DE LUCAS
Olá! Sou Lucas Costa, profissional apaixonado por Ciência de Dados e Machine Learning , com uma formação em Estatística pela Universidade Federal de Sergipe. Atualmente, atuo como Analista de Transformação na Iguá Saneamento, onde aplico minha expertise em Data Science e Business Intelligence para otimizar a tomada de decisões estratégicas. 📊
Minha trajetória é marcada por um profundo interesse em técnicas de Machine Learning, utilizando as linguagens R e Python para desenvolver soluções inovadoras. Além disso, possuo um sólido domínio em SQL, Power BI e DAX, ferramentas que me permitem transformar dados complexos em insights acionáveis e visualizações impactantes. 🎯
Acredito que a combinação de estatística, programação e visualização é essencial para revelar insights valiosos a partir dos dados. Estou sempre em busca de aprimorar minhas habilidades técnicas e criativas, desafiando-me a alcançar novos patamares de excelência. 🚀

## EXPERIÊNCIA PROFISSIONAL
1.	Iguá Saneamento
Analista de Transformação Sr. - fev/2026 - atualmente
•	Desenvolvimento de Soluções de Data Science para Otimização de Processos
•	Analise de Dados para Suporte à Tomada de Decisão Estratégica
•	Analise de Dados para Viabilidade de Projetos de Transformação
•	Analise de CAPEX e OPEX para Projetos de Transformação
•	Desenvolvimento de Dashboards e Relatórios para Monitoramento de Indicadores de Performance dos Projetos de Transformação
•	Gerenciamento do Power BI Service do Setor de Transformação
2.	Cencosud
Analista Estratégia de Risco PL. - abr/2025 - fev/2026
•	Adequação a CMN 4966/21
•	Modelagem da Probability of Default - PD
•	Modelagem da Loss Given Default - LGD
•	Modelagem da Exposure At Default - EAD
•	Modelagem da Provisão da Perda Esperada utilizando PD, LGD e EAD
•	Avaliação de Modelos Credit Score de Empresas Especializadas
•	Cálculo de Indicadores de Inadimplência 
•	Construção de Dashboard no Power BI 
•	Gerenciamento do Power BI Service
Analista Estratégia de Risco Jr. - jan/2024 - abr/2025
•	Construção do Modelo Behaviour Score para Risco de Crédito
•	Gerenciamento do Data Warehouse em SQL Server e MySQL
•	Cálculo de Indicadores de Inadimplência 
•	Provisão da Perda Esperada ao Risco de Crédito
•	Construção de Dashboard no Power BI 
•	Gerenciamento do Power BI Service

3.	Hospital Primavera
Estagiário de Analista de Business Intelligence - abr/2023 - dez/2023 
•	Criação de Consultas em Oracle SQL, SQL Server, MySQL
•	Automatização de Indicadores do Interact Direto dos Bancos de Dados
•	Construção de Dashboard no Power BI e Gerenciamento do Power BI Service
•	Automação de Tarefas via Power Automate

4.	Tribunal Regional Eleitoral - TRE 
Estagiário de Estatística - fev/2022 - mar/2023 
•	Gerenciamento dos Indicadores Estratégicos do TRE-SE
•	Gerenciamento das Metas do CNJ
•	Gerenciamento dos Indicadores Plano de Logística Sustentável do TRE-SE
•	Shiny App para Apuração de Votos em Tempo Real direto da API do TSE


## FORMAÇÃO ACADÊMICA
Universidade Federal de Sergipe - UFS - Bacharelado em Estatística - 2019/2024

## CURSOS E EXPERIÊNCIAS ADICIONAIS
•	TCC - Análise Comparativa Entre Modelos De Previsão ARMA-GARCH e Redes Neurais LSTM: Um Estudo de Caso Aplicado ao BOVA11
•	Formação - Power BI - Data University Cencosud
•	Curso - Data Warehouse Week - Xperium
•	Curso - Data Expert: Além do Básico - Xperium
•	Curso - Master Power BI De A à Z - Udemy 
•	Curso - Microsoft Excel 2016 Avançado - Fundação Bradesco
•	Curso - Introdução à programação com python - Digital Innovation One Inc. 
•	Curso - SQL SERVER Criando suas primeiras consultas - Digital Innovation One Inc.
•	Formação - Consultas com Oracle Database - Alura
•	Curso - Análise de Dados em Linguagem R - Enap 
•	Curso - Análise de Dados como Suporte a Tomada de Decisão - Enap 
•	Curso - Construindo Aplicações Web com R Utilizando o Pacote Shiny - UFS
•	Curso - Organização Apresentação e Tratamento de Dados Científicos - UFS


## PRINCIPAIS HABILIDADES
•	R Core Team 
•	Python
•	SQL Server
•	Power BI
•	QlickView,
•	Pentaho Data Integration
•	Figma
•	Excel
•	Power Point
•	Power Automate
•	Microsoft Forms

## PRINCIPAIS PROJETOS DESENVOLVIDOS
* Dashboard Power BI: 
1   Acompanhando a performance comercial em tempo real! 📊🚀 Este painel compara o faturamento realizado com as metas estabelecidas, trazendo insights sobre evolução mensal, desempenho por produto e ranking de vendedores. Além disso, destaca ticket médio, notas emitidas e projeções de forecast para o fechamento anual. 💼✨
2   Analisando o futuro financeiro com precisão! 📈✨ Este painel compara o poder da inteligência artificial, representada por uma rede neural LSTM, e da estatística, através do modelo GARCH, para prever a cotação do BOVA11. Utilizamos R e Python para treinar os modelos e o Power BI para visualizar os resultados. A junção perfeita de tecnologia e análise de dados. 💹🤖
3   Controlando as finanças pessoais com clareza e inteligência! 💰📊 Este painel acompanha a carteira ao longo do tempo, destacando receitas, despesas e a média mensal, além de detalhar a variação do saldo acumulado. Também traz insights sobre despesas por categoria, distribuição das transações e comparativos entre metas e valores realizados. Oferece uma visão completa para tomada de decisões financeiras mais conscientes e estratégicas. 📉✨


* Dashboard Streamlit: 
1    📈✨ Este painel interativo, desenvolvido com Streamlit, oferece uma análise aprofundada do desempenho de qualquer ação de sua escolha. Digite o ticker desejado para explorar dados históricos, visualizar gráficos de preços e acompanhar as previsões geradas pelo modelo ARMA-GARCH. Uma ferramenta poderosa e flexível para suas análises e projeções no mercado financeiro. 💹💻

* Web Site: 
1    Desenvolvimento de Web Site com Portifolio em dados Utilizando o Back-End com Python biblioteca Flask, e para o Front-End Utilizando HTML, CSS e Java Script. Sendo esse portifolio que você esta navengando.

* Analises de Risco de Crédito 
1    Construção e manutenção da modelagem de dados da carteira de crédito em SQL Server
2    Contrução de Modelos de Probabilidade de Inadimplência
3    Adequanção a nova Norma CMN 4.966/21 com modelagem esatistica de PE = PD x LGD x EAD
4    Validação de Modelos Credit Score de Bureaux de crédito para escolher a melhor empresa que presta este serviço

* Estatistica
1   Todos os Tipos de Amostragem: Amostragem Simples, Amostragem Estratificada, Amostrage Por Conglomerado
2   Modelos de Serie Temoral: SARIMA, ACF, PACF, Rede Neural Netework, Rede Neural LSTM
3   Modelos de Regreção Linear: Regressão Multipla, Regressão Logistica, Regressão de Poison
4   Analise Multivariada: PCA, K-mens, Agrupamentos 
5   Controle Estatístico de Qualidade
6   Econometria 

"""

# 4. O "CÉREBRO" DO CHATBOT (O ENDPOINT)
# O @app.route é o equivalente ao app.post() do Express
@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        # Pega a mensagem do JSON enviado pelo front-end
        user_message = request.json['message']

        # Monta o prompt com a personalidade e os dados
        prompt = f"""
        Você é a 'Puxa Saco', uma assistente virtual especialista no perfil profissional de Lucas.
        Sua tarefa é responder perguntas usando as informações fornecidas abaixo.
        Seja amigável, engraçada, um pouco "puxa-saco" (bajuladora), sem muitos elegios, de forma profissional, e precisa.
        Não invente informações que não estão no texto. Se a pergunta for sobre algo que não está nos dados, responda que você não tem essa informação
        
        --- DADOS PARA CONSULTA ---
        {dados_linkedin}
        --- FIM DOS DADOS ---

        Usuário: "{user_message}"
        
        Puxa Saco:"""

        # Envia o prompt para o Gemini e obtém a resposta
        # response = model.generate_content(prompt)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        bot_reply = response.text

        # Retorna a resposta no formato JSON que o front-end espera
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"error": "Desculpe, o Puxa Saco está em manutenção no momento."}), 500

