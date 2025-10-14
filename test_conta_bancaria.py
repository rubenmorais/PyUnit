import unittest
import timeit
from conta_bancaria import ContaBancaria, ValorInvalidoError, SaldoInsuficienteError

class TestContaBancaria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nTestes da Conta Bancária...\n")

    def setUp(self):
        self.conta1 = ContaBancaria("João", 1000)
        self.conta2 = ContaBancaria("Maria", 500)

    def test_depositos(self):
        for valor in [10, 200, 500]:
            with self.subTest(valor=valor):
                self.conta1.depositar(valor)
                self.assertEqual(self.conta1.consultar_saldo(), 1000 + valor)
                self.conta1.saldo = 1000  
    
    def test_levantar(self):
        self.conta1.levantar(300)
        self.assertEqual(self.conta1.consultar_saldo(), 700)
    
    def test_excecao_saldo_insuficiente(self):
        with self.assertRaises(SaldoInsuficienteError):
            self.conta1.levantar(2000)

    def test_excecao_valor_invalido(self):
        with self.assertRaises(ValorInvalidoError):
            self.conta1.depositar(-100) 
    
    def test_levantamento_invalido(self):
        with self.assertRaises(ValorInvalidoError):
            self.conta1.levantar(-100)
    
    def test_transferir(self):
        self.conta1.transferir(self.conta2, 300)
        self.assertEqual(self.conta1.consultar_saldo(), 700)
        self.assertEqual(self.conta2.consultar_saldo(), 800)

    def test_transferencia_para_mesma_conta(self):
        with self.assertRaises(ValorInvalidoError):
            self.conta1.transferir(self.conta1, 100)
    
    def test_transferir_saldo_insuficiente(self):
        with self.assertRaises(SaldoInsuficienteError):
            self.conta1.transferir(self.conta2, 1200)
    
    def test_transferencia_invalida(self):
        with self.assertRaises(ValorInvalidoError):
            self.conta1.transferir(self.conta2, -100)
    
    def test_transferencia_performance(self):
        tempo = timeit.timeit(lambda: self.conta1.transferir(self.conta2, 1), number=1000)
        self.assertLess(tempo, 2.0, "Transferência demasiado lenta")

    def test_consultar_saldo(self):
        self.assertEqual(self.conta1.consultar_saldo(), 200) #Erro de proposito

    @classmethod
    def tearDownClass(cls):
        print("\n✅ Testes finalizados com sucesso!\n")


if __name__ == "__main__":
    unittest.main()
