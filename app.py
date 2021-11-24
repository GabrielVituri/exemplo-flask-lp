from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista
pizzas = [
    {"nome": "4 Queijos", "disponivel": "Não"},
    {"nome": "Marguerita", "disponivel": "Sim"},
    {"nome": "Portuguesa", "disponivel": "Sim"},
]

# Index
@app.route('/')
def index():
    return render_template('index.html', lista=pizzas)

# Chamar Create
@app.route('/create')
def create():
    return render_template('create.html')

# Adicionar e Salvar Pizza
@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']
    disponivel = request.form['disponivel']
    novo = {"nome": nome, "disponivel": disponivel}  
    pizzas.append(novo)
    return redirect('https://5000-beige-spider-cgwqpr4p.ws-us17.gitpod.io/')

# Buscar pizza (nome)
@app.route('/buscar', methods=['POST'])
def buscar():
    lista = []
    buscar = request.form['buscar']
    for pizza in pizzas:
        if buscar in pizza['nome']:
            lista.append(pizza)
    return render_template('buscar.html', lista=lista)

# Chamar deletar
@app.route('/deletar')
def deletar():
    return render_template('deletar.html')

# Deletar pizza (indice)
@app.route('/excluir', methods=['POST'])
def excluir():  
    excluir = request.form['excluir']
    if excluir > '':
        excluir = int(excluir)
        if excluir <= len(pizzas) and excluir > 0:
            del pizzas[excluir-1]
            return redirect('https://5000-beige-spider-cgwqpr4p.ws-us17.gitpod.io/') 
    return render_template('erro.html')

app.run(debug=True)