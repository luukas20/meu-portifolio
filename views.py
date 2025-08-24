from main import app
from flask import render_template

# Rotas
@app.route('/', endpoint='pagina_home')
def homepage():
    return render_template("homepage.html")

@app.route('/projetos', endpoint='pagina_projetos')
def projetos():
    return render_template("projetos.html")