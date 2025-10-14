import logging
from exceptions import ValorInvalidoError, SaldoInsuficienteError

logger = logging.getLogger(__name__)

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        logger.info(f"Conta criada: {self.titular} com saldo inicial de {self.saldo}€")

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        logger.info(f"{self.titular} depositou {valor}€. Novo saldo: {self.saldo}€")

    def levantar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O valor do levantamento deve ser positivo.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        self.saldo -= valor
        logger.info(f"{self.titular} levantou {valor}€. Novo saldo: {self.saldo}€")

    def transferir(self, conta_destino, valor):
        if conta_destino == self:
            raise ValorInvalidoError("Não é possível transferir para a mesma conta.")
        if valor <= 0:
            raise ValorInvalidoError("O valor da transferência deve ser positivo.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para a transferência.")
        self.levantar(valor)
        conta_destino.depositar(valor)
        logger.info(f"{self.titular} transferiu {valor}€ para {conta_destino.titular}")

    def consultar_saldo(self):
        logger.info(f"{self.titular} consultou o saldo: {self.saldo}€")
        return self.saldo
