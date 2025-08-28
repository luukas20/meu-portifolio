from main import app
from flask import render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Rotas
@app.route('/', endpoint='pagina_home')
def homepage():
    return render_template("homepage.html")

# 1. CONFIGURAÇÃO INICIAL
load_dotenv() # Carrega as variáveis do arquivo .env

# 2. CONFIGURAÇÃO DA API DO GEMINI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

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
        Sua tarefa é responder perguntas usando as informações deste perfil do linkedin https://www.linkedin.com/in/luukas20/
        Seja amigável, um pouco "puxa-saco" (bajuladora) de forma profissional, e precisa.
        Não invente informações que não estão no linkedin. Se a pergunta for sobre algo que não está nos dados, responda que você não tem essa informação."""

        # Envia o prompt para o Gemini e obtém a resposta
        response = model.generate_content(prompt)
        bot_reply = response.text

        # Retorna a resposta no formato JSON que o front-end espera
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"error": "Desculpe, o Puxa Saco está em manutenção no momento."}), 500

