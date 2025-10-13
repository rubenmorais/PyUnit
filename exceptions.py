import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class ValorInvalidoError(Exception):
    """Erro lançado quando o valor informado é inválido."""
    pass

class SaldoInsuficienteError(Exception):
    """Erro lançado quando o saldo é insuficiente."""
    pass
