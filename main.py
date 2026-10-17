from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

# Os arquivos estáticos ficam em public/static: a Vercel serve public/** direto pela CDN
# (sem acionar o Flask); no Render e no desenvolvimento o próprio Flask serve a mesma pasta
app = Flask(__name__, static_folder="public/static", static_url_path="/static")
# Atrás do proxy da hospedagem: usa o IP real do visitante (limite de uso do chat)
# e o protocolo/host reais (endereços absolutos da prévia de compartilhamento saem em https)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

from views import *

if __name__ == "__main__":
    app.run()
