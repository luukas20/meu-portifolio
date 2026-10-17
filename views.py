from main import app
from flask import render_template, request, jsonify
from dotenv import load_dotenv
from functools import lru_cache
from pathlib import Path
import os
from google import genai
from google.genai import errors, types
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from conteudo import ESPECIALIDADES, PROJETOS, REDES, SOBRE_MIM

# 1. CONFIGURAÇÃO INICIAL
load_dotenv() # Carrega as variáveis do arquivo .env

# Modelos do Gemini: troque pelas variáveis GEMINI_MODEL / GEMINI_MODEL_RESERVA sem mexer no código
MODELO_GEMINI = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
# Reserva usada se o principal estiver sem crédito (402), fora do ar (404, 500, 503) ou no limite (429)
MODELO_RESERVA = os.getenv("GEMINI_MODEL_RESERVA", "gemini-3.5-flash-lite")
CODIGOS_COM_RESERVA = {402, 404, 429, 500, 503}
TAMANHO_MAXIMO_MENSAGEM = 500
PASTA_PROMPTS = Path(__file__).resolve().parent / "prompts"

# Limite de uso do chat por IP (em memória; vale por instância do servidor)
limiter = Limiter(get_remote_address, app=app, storage_uri="memory://")

# Rotas
@app.route('/', endpoint='pagina_home')
def homepage():
    return render_template(
        "homepage.html",
        especialidades=ESPECIALIDADES,
        sobre_mim=SOBRE_MIM,
        redes_sociais=REDES,
        projetos=PROJETOS,
    )

# 2. CLIENTE DO GEMINI
# Criado só na primeira mensagem: sem a chave, o site abre e só o chat falha
@lru_cache(maxsize=1)
def obter_cliente():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 3. PROMPT DO CHATBOT
# Persona e conhecimento ficam em prompts/*.md (editar o .md e reiniciar o servidor)
@lru_cache(maxsize=1)
def carregar_instrucoes():
    persona = (PASTA_PROMPTS / "persona.md").read_text(encoding="utf-8").strip()
    conhecimento = (PASTA_PROMPTS / "conhecimento.md").read_text(encoding="utf-8").strip()
    return f"{persona}\n\n--- DADOS PARA CONSULTA ---\n{conhecimento}\n--- FIM DOS DADOS ---"

def gerar_resposta(mensagem):
    # Persona e dados vão na instrução do sistema; o usuário só em `contents`
    config = types.GenerateContentConfig(
        system_instruction=carregar_instrucoes(),
        max_output_tokens=1024,
    )
    modelos = [MODELO_GEMINI]
    if MODELO_RESERVA and MODELO_RESERVA != MODELO_GEMINI:
        modelos.append(MODELO_RESERVA)

    for posicao, modelo in enumerate(modelos):
        try:
            return obter_cliente().models.generate_content(model=modelo, contents=mensagem, config=config)
        except errors.APIError as erro:
            if erro.code not in CODIGOS_COM_RESERVA or posicao == len(modelos) - 1:
                raise
            app.logger.warning("Modelo %s falhou (%s); usando %s", modelo, erro.code, modelos[posicao + 1])

# 4. O "CÉREBRO" DO CHATBOT (O ENDPOINT)
@app.route("/api/chat", methods=["POST"])
@limiter.limit("10 per minute;100 per day")
def chat():
    # Valida o corpo antes de gastar a cota do Gemini
    corpo = request.get_json(silent=True)
    mensagem = corpo.get("message") if isinstance(corpo, dict) else None
    if not isinstance(mensagem, str) or not mensagem.strip():
        return jsonify({"error": "Envie uma mensagem de texto."}), 400
    mensagem = mensagem.strip()
    if len(mensagem) > TAMANHO_MAXIMO_MENSAGEM:
        return jsonify({"error": f"A mensagem pode ter no máximo {TAMANHO_MAXIMO_MENSAGEM} caracteres."}), 400

    try:
        resposta = gerar_resposta(mensagem)
        texto = (resposta.text or "").strip()
        if not texto:
            # Resposta vazia (ex.: bloqueio de segurança do modelo)
            return jsonify({"reply": "Não consegui formular uma resposta para isso. Pode reformular a pergunta?"})
        return jsonify({"reply": texto})

    except Exception:
        app.logger.exception("Erro ao consultar o Gemini")
        return jsonify({"error": "Desculpe, o Puxa Saco está em manutenção no momento."}), 500

@app.errorhandler(429)
def limite_excedido(erro):
    return jsonify({"error": "Muitas mensagens em pouco tempo. Aguarde um instante e tente de novo."}), 429
