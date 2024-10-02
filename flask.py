from flask import Flask, jsonify, request

app = Flask(__name__)

# Estruturas de dados estáticas
professores = {
    "professores": [
        {"id": 1, "nome": "Lucas", "idade": 45, "materia": "Matemática", "observacoes": "Doutorado em Matemática"},
        {"id": 2, "nome": "Cicero", "idade": 39, "materia": "Física", "observacoes": "Mestre em Física Aplicada"}
    ]
}

turmas = {
    "turmas": [
        {"id": 1, "descricao": "Turma A - Matemática", "professor_id": 1, "ativo": True},
        {"id": 2, "descricao": "Turma B - Física", "professor_id": 2, "ativo": False}
    ]
}

alunos = {
    "alunos": [
        {"id": 1, "nome": "João", "idade": 16, "turma_id": 1, "data_nascimento": "2008-01-15", 
         "nota_primeiro_semestre": 8.5, "nota_segundo_semestre": 9.0, "media_final": 8.75},
        {"id": 2, "nome": "Maria", "idade": 17, "turma_id": 2, "data_nascimento": "2007-05-22", 
         "nota_primeiro_semestre": 7.0, "nota_segundo_semestre": 7.5, "media_final": 7.25}
    ]
}

# Funções auxiliares para gerar novos IDs
def get_new_id(items):
    if items:
        return max(item["id"] for item in items) + 1
    return 1

# CRUD para Professor
@app.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(professores)

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores['professores'] if p['id'] == id), None)
    if professor:
        return jsonify(professor)
    return jsonify({'message': 'Professor não encontrado'}), 404

@app.route('/professores', methods=['POST'])
def create_professor():
    new_professor = request.json
    new_professor["id"] = get_new_id(professores["professores"])
    professores["professores"].append(new_professor)
    return jsonify(new_professor), 201

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    professor = next((p for p in professores['professores'] if p['id'] == id), None)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404
    professor.update(request.json)
    return jsonify(professor)

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    professor = next((p for p in professores['professores'] if p['id'] == id), None)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404
    professores['professores'].remove(professor)
    return jsonify({'message': 'Professor deletado com sucesso'})

# CRUD para Turma
@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(turmas)

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = next((t for t in turmas['turmas'] if t['id'] == id), None)
    if turma:
        return jsonify(turma)
    return jsonify({'message': 'Turma não encontrada'}), 404

@app.route('/turmas', methods=['POST'])
def create_turma():
    new_turma = request.json
    new_turma["id"] = get_new_id(turmas["turmas"])
    turmas["turmas"].append(new_turma)
    return jsonify(new_turma), 201

@app.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    turma = next((t for t in turmas['turmas'] if t['id'] == id), None)
    if not turma:
        return jsonify({'message': 'Turma não encontrada'}), 404
    turma.update(request.json)
    return jsonify(turma)

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    turma = next((t for t in turmas['turmas'] if t['id'] == id), None)
    if not turma:
        return jsonify({'message': 'Turma não encontrada'}), 404
    turmas['turmas'].remove(turma)
    return jsonify({'message': 'Turma deletada com sucesso'})

# CRUD para Aluno
@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = next((a for a in alunos['alunos'] if a['id'] == id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({'message': 'Aluno não encontrado'}), 404

@app.route('/alunos', methods=['POST'])
def create_aluno():
    new_aluno = request.json
    new_aluno["id"] = get_new_id(alunos["alunos"])
    alunos["alunos"].append(new_aluno)
    return jsonify(new_aluno), 201

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    aluno = next((a for a in alunos['alunos'] if a['id'] == id), None)
    if not aluno:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    aluno.update(request.json)
    return jsonify(aluno)

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    aluno = next((a for a in alunos['alunos'] if a['id'] == id), None)
    if not aluno:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    alunos['alunos'].remove(aluno)
    return jsonify({'message': 'Aluno deletado com sucesso'})

# Rota principal
@app.route('/')
def index():
    return "Sistema de gerenciamento escolar com CRUD em Flask"

if __name__ == '__main__':
    app.run(debug=True)
