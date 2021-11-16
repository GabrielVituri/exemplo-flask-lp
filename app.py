from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pizzas = [
    {"nome": "4 Queijos", "disponivel": False},
    {"nome": "Marguerita", "disponivel": False},
    {"nome": "Portuguesa", "disponivel": True},
]

@app.route('/')
def index():
    return render_template('index.html', lista=pizzas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']
    disponivel = request.form['disponivel']
    { "nome": nome, "disponivel": True }
    { "nome": nome, "disponivel": False }
    pizzas.append(tarefa)

    return redirect('https://5000-brown-lemur-kiu2j61j.ws-us18.gitpod.io/')

#jsaisjdifdsfsa



# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)