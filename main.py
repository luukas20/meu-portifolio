from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
# Atrás do proxy da hospedagem: usa o IP real do visitante (limite de uso do chat)
# e o protocolo/host reais (endereços absolutos da prévia de compartilhamento saem em https)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

from views import *

if __name__ == "__main__":
    app.run()
