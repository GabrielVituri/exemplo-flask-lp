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
    nome = requests.get['nome']
    disponivel = request.form['disponivel']
    novo = {"nome": nome, "disponivel": disponivel}  
    pizzas.append(novo)
    return redirect('https://5000-beige-spider-cgwqpr4p.ws-us18.gitpod.io/')
    
@app.rout('/deletar')
def deletar():
    return render_template('deletar.html')

@app.route('/excluir')
def excluir():  
    excluir = ['indice']
    for pizza in pizzas:
        if excluir == pizzas['nome']:
            pizzas.remove(pizza['nome'])

    return redirect('https://5000-beige-spider-cgwqpr4p.ws-us18.gitpod.io/') 


app.run(debug=True)

# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)