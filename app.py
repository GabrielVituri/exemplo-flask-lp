from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pizzas = [
    {"nome": "4 Queijos", "disponivel": "Não"},
    {"nome": "Marguerita", "disponivel": "Sim"},
    {"nome": "Portuguesa", "disponivel": "Sim"},
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
    novo = {"nome": nome, "disponivel": disponivel}  
    pizzas.append(novo)
    return redirect('https://5000-beige-spider-cgwqpr4p.ws-us18.gitpod.io/')
    
@app.route('/excluir', methods=['POST'])
def excluir():  
    return redirect('https://5000-beige-spider-cgwqpr4p.ws-us18.gitpod.io/') 


app.run(debug=True)

# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)