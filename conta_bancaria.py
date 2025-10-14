from exceptions import ValorInvalidoError, SaldoInsuficienteError

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor do depósito deve ser positivo.")
        self.saldo += valor

    def levantar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor do levantamento deve ser positivo.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        self.saldo -= valor

    def transferir(self, conta_destino, valor):
        if conta_destino == self:
            raise ValorInvalidoError("Não é possível transferir para a mesma conta.")
        if valor <= 0:
            raise ValorInvalidoError("O valor da transferência deve ser positivo.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para a transferência.")
        self.levantar(valor)
        conta_destino.depositar(valor)

    def consultar_saldo(self):
        return self.saldo



"""

python -m unittest test_conta_bancaria.py


pip install coverage
coverage run -m unittest discover
coverage html

"""