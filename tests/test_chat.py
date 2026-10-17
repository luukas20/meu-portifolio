import pytest
from google.genai import errors

import views
from main import app


class RespostaFalsa:
    def __init__(self, text):
        self.text = text


class ClienteFalso:
    """Imita client.models.generate_content sem chamar o Gemini.

    `erro` vale para todos os modelos; `erros_por_modelo` mapeia modelo -> erro.
    """

    def __init__(self, texto="Olá! Sou a Puxa Saco.", erro=None, erros_por_modelo=None):
        self.texto = texto
        self.erro = erro
        self.erros_por_modelo = erros_por_modelo or {}
        self.chamadas = []
        self.models = self

    def generate_content(self, **kwargs):
        self.chamadas.append(kwargs)
        erro = self.erros_por_modelo.get(kwargs["model"], self.erro)
        if erro:
            raise erro
        return RespostaFalsa(self.texto)


def erro_api(codigo):
    return errors.ClientError(codigo, {"error": {"message": "teste", "status": "TESTE"}})


@pytest.fixture
def http():
    app.testing = True
    views.limiter.reset()
    views.limiter.enabled = False
    yield app.test_client()
    views.limiter.enabled = True
    views.limiter.reset()


def usar_cliente(monkeypatch, cliente):
    monkeypatch.setattr(views, "obter_cliente", lambda: cliente)
    return cliente


def test_home_responde_200(http):
    resposta = http.get("/")
    assert resposta.status_code == 200
    assert "Lucas" in resposta.get_data(as_text=True)


@pytest.mark.parametrize("corpo", [
    {"message": ""},
    {"message": "   "},
    {"message": 123},
    {"outro": "campo"},
    ["lista"],
])
def test_corpo_invalido_retorna_400(http, monkeypatch, corpo):
    falso = usar_cliente(monkeypatch, ClienteFalso())
    resposta = http.post("/api/chat", json=corpo)
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert falso.chamadas == []


def test_corpo_que_nao_e_json_retorna_400(http, monkeypatch):
    falso = usar_cliente(monkeypatch, ClienteFalso())
    resposta = http.post("/api/chat", data="oi", content_type="text/plain")
    assert resposta.status_code == 400
    assert falso.chamadas == []


def test_mensagem_longa_retorna_400(http, monkeypatch):
    falso = usar_cliente(monkeypatch, ClienteFalso())
    resposta = http.post("/api/chat", json={"message": "a" * (views.TAMANHO_MAXIMO_MENSAGEM + 1)})
    assert resposta.status_code == 400
    assert falso.chamadas == []


def test_resposta_ok_separa_instrucoes_da_mensagem(http, monkeypatch):
    falso = usar_cliente(monkeypatch, ClienteFalso(texto="  Ele trabalha na Iguá.  "))
    resposta = http.post("/api/chat", json={"message": "Onde o Lucas trabalha?"})

    assert resposta.status_code == 200
    assert resposta.get_json() == {"reply": "Ele trabalha na Iguá."}

    chamada = falso.chamadas[0]
    instrucoes = chamada["config"].system_instruction
    assert chamada["contents"] == "Onde o Lucas trabalha?"
    assert "Puxa Saco" in instrucoes
    assert "RESUMO PROFISSIONAL" in instrucoes
    assert "Onde o Lucas trabalha?" not in instrucoes


def test_resposta_vazia_devolve_mensagem_amigavel(http, monkeypatch):
    usar_cliente(monkeypatch, ClienteFalso(texto=None))
    resposta = http.post("/api/chat", json={"message": "oi"})
    assert resposta.status_code == 200
    assert resposta.get_json()["reply"]


def test_erro_do_gemini_retorna_500_amigavel(http, monkeypatch):
    usar_cliente(monkeypatch, ClienteFalso(erro=RuntimeError("falhou")))
    resposta = http.post("/api/chat", json={"message": "oi"})
    assert resposta.status_code == 500
    assert "manutenção" in resposta.get_json()["error"]


def modelos_chamados(cliente):
    return [chamada["model"] for chamada in cliente.chamadas]


def test_modelo_principal_sem_credito_usa_a_reserva(http, monkeypatch):
    falso = usar_cliente(monkeypatch, ClienteFalso(
        texto="Resposta da reserva",
        erros_por_modelo={views.MODELO_GEMINI: erro_api(402)},
    ))
    resposta = http.post("/api/chat", json={"message": "oi"})
    assert resposta.status_code == 200
    assert resposta.get_json() == {"reply": "Resposta da reserva"}
    assert modelos_chamados(falso) == [views.MODELO_GEMINI, views.MODELO_RESERVA]


def test_erro_que_nao_justifica_reserva_nao_troca_de_modelo(http, monkeypatch):
    falso = usar_cliente(monkeypatch, ClienteFalso(erro=erro_api(400)))
    resposta = http.post("/api/chat", json={"message": "oi"})
    assert resposta.status_code == 500
    assert modelos_chamados(falso) == [views.MODELO_GEMINI]


def test_principal_e_reserva_falhando_retorna_500(http, monkeypatch):
    falso = usar_cliente(monkeypatch, ClienteFalso(erro=erro_api(402)))
    resposta = http.post("/api/chat", json={"message": "oi"})
    assert resposta.status_code == 500
    assert modelos_chamados(falso) == [views.MODELO_GEMINI, views.MODELO_RESERVA]


def test_limite_de_uso_retorna_429_em_json(http, monkeypatch):
    usar_cliente(monkeypatch, ClienteFalso())
    views.limiter.enabled = True
    status = [http.post("/api/chat", json={"message": "oi"}).status_code for _ in range(11)]
    assert status[:10] == [200] * 10
    assert status[10] == 429
    ultima = http.post("/api/chat", json={"message": "oi"})
    assert ultima.get_json()["error"]


@pytest.mark.parametrize("arquivo", ["persona.md", "conhecimento.md"])
def test_arquivos_de_prompt_existem_e_nao_estao_vazios(arquivo):
    caminho = views.PASTA_PROMPTS / arquivo
    assert caminho.read_text(encoding="utf-8").strip()
