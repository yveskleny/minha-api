from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana", "curso": "Técnico em Informática"},
    {"id": 2, "nome": "Bruno", "curso": "Técnico em Desenvolvimento"},
    {"id": 3, "nome": "Carla", "curso": "Técnico em Informática"}
]

tarefas = [
    {"id": 1,"titulo": "Tarefa 1" , "descricao": "Fazer a tarefa 1", "concluida": False},
    {"id": 2,"titulo": "Tarefa 2" , "descricao": "Fazer a tarefa 2", "concluida": True},
    {"id": 3,"titulo": "Tarefa 3" , "descricao": "Fazer a tarefa 3", "concluida": False}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Esta mensagem veio do alem!",
        "status": "ok"
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "message": "Healthy"
    })


@app.route('/aluno', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)


@app.route('/aluno/<int:id>', methods=['GET'])
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)
    return jsonify({"Erro": "Aluno não encontrado"}), 404

@app.route("/aluno", methods=["POST"])
def criar_aluno():
    dados = request.get_json()

    if not dados:
        return jsonify({"Erro": "Dados inválidos!"}), 400
    
    if "nome" not in dados or "curso" not in dados:
        return jsonify({"Erro": "Campos obrigatórios não preenchidos!"}), 400
    
    novo_aluno = {
        "id": len(alunos) + 1,
        "nome": dados["nome"],
        "curso": dados["curso"]
    }

    alunos.append(novo_aluno)

    return jsonify(novo_aluno), 201


@app.route("/tarefa", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefa/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return jsonify(tarefa)

    return jsonify({"Erro": "Tarefa não encotrada!"}), 404


@app.route("/tarefa", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    if not dados:
        return jsonify({"Erro": "Dados inválidos!"}), 400
    
    if "titulo" not in dados or "descricao" not in dados:
        return jsonify({"Erro": "Campos obrigatórios não preenchidos!"}), 400
    

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


if __name__ == '__main__':
    app.run(debug=True)



