from flask import Flask, jsonify

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana", "curso": "Técnico em Informática"},
    {"id": 2, "nome": "Bruno", "curso": "Técnico em Desenvolvimento"},
    {"id": 3, "nome": "Carla", "curso": "Técnico em Informática"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Esta mensagem veio do alem!",
        "status": "ok"
    })


@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "message": "Healthy"
    })


@app.route('/aluno')
def listar_alunos():
    return jsonify(alunos)


@app.route('/aluno/<int:id>')
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)


