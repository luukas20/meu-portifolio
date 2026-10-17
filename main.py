from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
# Atrás do proxy da hospedagem, usa o IP real do visitante (limite de uso do chat)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

from views import *

if __name__ == "__main__":
    app.run()
