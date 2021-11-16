from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {"nome": "4 Queijos", "disponivel": False},
    {"nome": "Marguerita", "disponivel": False},
    {"nome": "Portuguesa", "disponivel": True},
]

@app.route('/')
def index():
    return render_template('index.html', lista=tarefas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']
    disponivel = request.form['disponivel']

    if "disponivel" == True: tarefa = { "nome": nome, "disponivel": True }
    else: tarefa = { "nome": nome, "disponivel": False }
    tarefas.append(tarefa)

    return redirect('https://5000-brown-lemur-kiu2j61j.ws-us18.gitpod.io/')

#jsaisjdi



# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)