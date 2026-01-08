from flask import Flask, request, jsonify
from micro_servico.repository import (
    create_table,
    insert_cliente,
    listar_clientes,
    buscar_cliente_por_id,
    atualizar_cliente,
    delete_cliente
)

app = Flask(__name__)
create_table()


@app.route("/status", methods=["GET"])
def status():
    return jsonify({"mensagem": "Microserviço de Armazenamento está funcionando."})

@app.route("/clientes", methods=["POST"])
def criar_cliente():
    dados = request.get_json()

    cliente_id = insert_cliente(
        dados.get("nome"),
        dados.get("telefone"),
        dados.get("correntista"),
        dados.get("score_credito"),
        dados.get("saldo_cc")
    )

    dados["id"] = cliente_id
    return jsonify(dados), 201

@app.route("/clientes", methods=["GET"])
def listar():
    linhas = listar_clientes()
    lista = []

    for linha in linhas:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "telefone": linha[2],
            "correntista": linha[3],
            "score_credito": linha[4],
            "saldo_cc": linha[5],
        })

    return jsonify(lista)

@app.route("/clientes/<id>", methods=["GET"])
def buscar(id):
    linha = buscar_cliente_por_id(int(id))

    if not linha:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    cliente = {
        "id": linha[0],
        "nome": linha[1],
        "telefone": linha[2],
        "correntista": linha[3],
        "score_credito": linha[4],
        "saldo_cc": linha[5],
    }

    return jsonify(cliente)

@app.route("/clientes/<id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()

    atualizar_cliente(
        int(id),
        dados.get("nome"),
        dados.get("telefone"),
        dados.get("correntista"),
        dados.get("score_credito"),
        dados.get("saldo_cc")
    )

    dados["id"] = int(id)
    return jsonify(dados), 200

@app.route("/clientes/<id>", methods=["DELETE"])
def excluir(id):
    linha = buscar_cliente_por_id(int(id))

    if not linha:
        return jsonify({"erro": "Cliente não encontrado"}), 404

    delete_cliente(int(id))

    return jsonify({"sucesso": "Cliente deletado"}), 200



if __name__ == "__main__":
    app.run(debug=True)