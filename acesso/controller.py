from flask import Flask, request, jsonify
from .service import criar_cliente_service, atualizar_cliente_service, calcular_score, operacao_service
from .client import listar_clientes, buscar_cliente_por_id, deletar_cliente

app = Flask(__name__)

@app.route("/clientes", methods=["POST"])
def criar_cliente_controller():
    dados = request.get_json()
    result = criar_cliente_service(dados)
    if type(result) is str:
        return jsonify(result), 400
    else:
        return jsonify(result), 201

@app.route("/clientes", methods=["GET"])
def listar_clientes_controller():
    result = listar_clientes()
    return jsonify(result), 200

@app.route("/clientes/<id>", methods=["GET"])
def buscar_cliente_controller(id):
    result = buscar_cliente_por_id(id)
    if "erro" in result:
        return jsonify(result), 404
    else:
        return jsonify(result), 200

@app.route("/clientes/<id>", methods=["PUT"])
def atualizar_cliente_controller(id):
    dados = request.get_json()
    result = atualizar_cliente_service(id, dados)
    if type(result) is str:
        return jsonify(result), 400
    if "erro" in result:
        return jsonify(result), 404
    return jsonify(result), 200

@app.route("/clientes/<id>", methods=["DELETE"])
def deletar_cliente_controller(id):
    result = deletar_cliente(id)
    if "erro" in result:
        return jsonify(result), 404
    else:
        return jsonify(result), 200

@app.route("/clientes/<id>/score", methods=["GET"])
def score_controller(id):
    result = buscar_cliente_por_id(id)
    if "erro" in result:
        return jsonify(result), 404
    else:
        saldo = result["saldo_cc"]
        score = calcular_score(saldo)
        score_resposta = {
            "id": id,
            "score": score
        }
        return jsonify(score_resposta), 200

@app.route("/clientes/<id>/operacao", methods=["POST"])
def operacao_controller(id):
    dados = request.get_json()
    result = operacao_service(id, dados)
    if type(result) is str:
        return jsonify({"erro": result}), 400
    if "erro" in result:
        return jsonify(result), 404
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)
