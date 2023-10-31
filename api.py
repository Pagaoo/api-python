from flask import Flask, jsonify, request

from bd_connection import get_db_connection


app  = Flask(__name__)

get_db_connection()

@app.route('/livros', methods=['GET'])
def obter_livros():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros ORDER BY id ASC")
    livros = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE id = %s", (id,))
    livro = cursor.fetchone()
    cursor.close()
    conn.close()
    if livro is not None:
        return jsonify(livro)
    else:
        return jsonify({"message": "Livros não encontrado"}), 404

@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor) VALUES (%s, %s)", (novo_livro['titulo'], novo_livro['autor']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Livro adicionado com sucesso"})
        
@app.route('/livros/titlo/<int:id>', methods=['PUT'])
def editar_titulo_do_livro_por_id(id):
    livro_alterado = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET titulo = %s WHERE id = %s", (livro_alterado['titulo'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Titulo do livro alterado com sucesso"})     
      
@app.route('/livros/autor/<int:id>', methods=['PUT'])
def editar_autor_do_livro_por_id(id):
    livro_alterado = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET autor = %s WHERE id = %s", (livro_alterado['autor'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Autor do livro alterado com sucesso"})     
          
        
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro_por_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Livro excluido com sucesso"})

app.run(port=5000, host='localhost', debug=True)