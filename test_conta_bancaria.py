import unittest
import timeit
import logging
import time
from conta_bancaria import ContaBancaria, ValorInvalidoError, SaldoInsuficienteError
from app import app

class TestContaBancaria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.start_time = time.time()
        print("\nTestes da Conta Bancária...\n")

    def setUp(self):
        self.conta1 = ContaBancaria("João", 1000)
        self.conta2 = ContaBancaria("Maria", 500)

    def test_depositos(self):
        """Testa depósitos válidos"""
        for valor in [10, 200, 500]:
            with self.subTest(valor=valor):
                self.conta1.depositar(valor)
                self.assertEqual(self.conta1.consultar_saldo(), 1000 + valor)
                self.conta1.saldo = 1000

    def test_levantar(self):
        """Testa levantamento válido"""
        self.conta1.levantar(300)
        self.assertEqual(self.conta1.consultar_saldo(), 700)

    def test_excecao_saldo_insuficiente(self):
        """Levantar acima do saldo deve lançar erro"""
        with self.assertRaises(SaldoInsuficienteError):
            self.conta1.levantar(2000)

    def test_excecao_valor_invalido(self):
        """Depósito de valor negativo deve lançar erro"""
        with self.assertRaises(ValorInvalidoError):
            self.conta1.depositar(-100)

    def test_levantamento_invalido(self):
        """Levantamento de valor negativo deve lançar erro"""
        with self.assertRaises(ValorInvalidoError):
            self.conta1.levantar(-100)

    def test_transferir(self):
        """Testa transferência válida entre contas"""
        self.conta1.transferir(self.conta2, 300)
        self.assertEqual(self.conta1.consultar_saldo(), 700)
        self.assertEqual(self.conta2.consultar_saldo(), 800)

    def test_transferencia_para_mesma_conta(self):
        """Transferir para mesma conta deve lançar erro"""
        with self.assertRaises(ValorInvalidoError):
            self.conta1.transferir(self.conta1, 100)

    def test_transferir_saldo_insuficiente(self):
        """Transferência com saldo insuficiente deve lançar erro"""
        with self.assertRaises(SaldoInsuficienteError):
            self.conta1.transferir(self.conta2, 1200)

    def test_transferencia_invalida(self):
        """Transferência com valor negativo deve lançar erro"""
        with self.assertRaises(ValorInvalidoError):
            self.conta1.transferir(self.conta2, -100)

    def test_transferencia_performance(self):
        """Testa performance da transferência (1000 vezes em < 2s), sem logs"""
        logging.disable(logging.CRITICAL)  
        try:
            tempo = timeit.timeit(lambda: self.conta1.transferir(self.conta2, 1), number=1000)
            self.assertLess(tempo, 2.0, "Transferência demasiado lenta")
        finally:
            logging.disable(logging.NOTSET)  

    
    """def test_consultar_saldo(self): 
        self.assertEqual(self.conta1.consultar_saldo(), 200)""" #Erro de proposito

    # --- Testes da API Flask ---

    def test_saldo_api(self):
        """Consulta saldo para conta existente deve retornar 200 e saldo"""
        response = self.client.get('/saldo/joao')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['titular'], 'Joao')
        self.assertIn('saldo', data)

    def test_saldo_api_conta_inexistente(self):
        """Consulta saldo para conta inexistente deve retornar 404"""
        response = self.client.get('/saldo/naoexiste')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('erro', data)

    def test_transferir_api(self):
        """Transferência válida via API deve retornar 200 e mensagem"""
        response = self.client.post('/transferir', json={
            'origem': 'joao',
            'destino': 'maria',
            'valor': 100
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['mensagem'], 'Transferência concluída')

    def test_transferir_api_valor_invalido(self):
        """Transferência com valor inválido deve retornar 400 e erro"""
        response = self.client.post('/transferir', json={
            'origem': 'joao',
            'destino': 'maria',
            'valor': -100
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('erro', data)

    @classmethod
    def tearDownClass(cls):
        duracao = time.time() - cls.start_time
        print(f"\n✅ Testes finalizados com sucesso! Tempo total: {duracao:.2f} segundos\n")


if __name__ == "__main__":
    unittest.main()
