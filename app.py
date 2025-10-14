from flask import Flask, request, jsonify
from conta_bancaria import ContaBancaria, ValorInvalidoError, SaldoInsuficienteError

app = Flask(__name__)

contas = {"joao": ContaBancaria("Joao", 1000), "maria": ContaBancaria("Maria", 500)}

@app.route("/saldo/<titular>")
def saldo(titular):
    conta = contas.get(titular.lower())
    if not conta:
        return jsonify({"erro": "Conta não encontrada"}), 404
    return jsonify({"titular": conta.titular, "saldo": conta.consultar_saldo()})

@app.route("/transferir", methods=["POST"])
def transferir():
    data = request.get_json()
    origem = contas.get(data["origem"].lower())
    destino = contas.get(data["destino"].lower())
    valor = data["valor"]
    try:
        origem.transferir(destino, valor)
        return jsonify({"mensagem": "Transferência concluída"}), 200
    except (ValorInvalidoError, SaldoInsuficienteError) as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
