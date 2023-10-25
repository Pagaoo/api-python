from flask import Flask, jsonify, request


app  = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': "Senhor dos Anéis",
        'autor': "J. R. R. Tolkien"
    },
    {
        'id': 2,
        'titulo': "As crônias de Nárnia",
        'autor': "C. S. Lewis"
    },
    {
        'id': 3,
        'titulo': "A song of ice and fire",
        'autor': "George R. R. Martin"
    }
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        

@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
        
        
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)