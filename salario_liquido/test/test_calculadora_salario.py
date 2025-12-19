import unittest
from src.calculadora_salario import calcular_salario_liquido, _validar_salario, _validar_dependentes

class TestCalculadoraSalario(unittest.TestCase):

    # =========================================================================
    # Testes de Validação (100% de cobertura de exceções)
    # =========================================================================

    def test_validar_salario_negativo(self):
        with self.assertRaisesRegex(ValueError, "Salário bruto deve ser maior que zero"):
            _validar_salario(-1000.00)

    def test_validar_salario_zero(self):
        with self.assertRaisesRegex(ValueError, "Salário bruto deve ser maior que zero"):
            _validar_salario(0.00)

    def test_validar_dependentes_negativo(self):
        with self.assertRaisesRegex(ValueError, "Número de dependentes não pode ser negativo"):
            _validar_dependentes(-1)

    # =========================================================================
    # Testes de Compatibilidade V1 (Modo V1) - IR sobre Base de Cálculo
    # =========================================================================

    def test_v1_salario_ate_2000_sem_irrf(self):
        # Salário 2000. INSS: 160.00. BC_IR: 1840.00. IR V1: 0.00. Líquido: 1840.00
        salario_bruto = 2000.00
        resultado = calcular_salario_liquido(salario_bruto, modo_v1=True)
        self.assertEqual(resultado, 1840.00)

    def test_v1_salario_acima_2000_com_irrf(self):
        # Salário 3000. INSS: 240.00. BC_IR: 2760.00. IR V1: 276.00. Líquido: 2484.00
        salario_bruto = 3000.00
        resultado = calcular_salario_liquido(salario_bruto, modo_v1=True)
        self.assertEqual(resultado, 2484.00)

    def test_v1_inss_deve_respeitar_teto(self):
        # Salário 10000. INSS: 500.00. BC_IR: 9500.00. IR V1: 950.00. Líquido: 8550.00
        salario_bruto = 10000.00
        resultado = calcular_salario_liquido(salario_bruto, modo_v1=True)
        self.assertEqual(resultado, 8550.00)

    # =========================================================================
    # Testes V2 (Modo Padrão) - IR sobre Base de Cálculo
    # =========================================================================

    def test_v2_faixa_1_sem_irrf(self):
        # Salário 1500. INSS: 120.00. BC_IR: 1380.00. IR V2 Faixa 1: 0.00. Líquido: 1380.00
        salario_bruto = 1500.00
        resultado = calcular_salario_liquido(salario_bruto)
        self.assertEqual(resultado, 1380.00)

    def test_v2_faixa_2_com_irrf(self):
        # Salário 3000. INSS: 240.00. BC_IR: 2760.00. IR V2 Faixa 2: 276.00. Líquido: 2484.00
        salario_bruto = 3000.00
        resultado = calcular_salario_liquido(salario_bruto)
        self.assertEqual(resultado, 2484.00)

    def test_v2_faixa_3_com_irrf(self):
        # Salário 5000. INSS: 400.00. BC_IR: 4600.00. IR V2 Faixa 3: 920.00. Líquido: 3680.00
        salario_bruto = 5000.00
        resultado = calcular_salario_liquido(salario_bruto)
        self.assertEqual(resultado, 3680.00)

    def test_v2_com_dependentes(self):
        # Salário 3000. INSS: 240.00. BC_IR: 2760.00. IR Bruto: 276.00.
        # Desconto dependente (2): 27.60. IR Final: 248.40. Líquido: 2511.60
        salario_bruto = 3000.00
        dependentes = 2
        resultado = calcular_salario_liquido(salario_bruto, dependentes=dependentes)
        self.assertEqual(resultado, 2511.60)

    def test_v2_desconto_dependente_nao_negativo(self):
        # Salário 1500. INSS: 120.00. BC_IR: 1380.00. IR Bruto: 0.00. IR Final: 0.00. Líquido: 1380.00
        salario_bruto = 1500.00
        dependentes = 5
        resultado = calcular_salario_liquido(salario_bruto, dependentes=dependentes)
        self.assertEqual(resultado, 1380.00)

    def test_v2_com_vale_transporte(self):
        # Salário 3000. INSS: 240.00. BC_IR: 2760.00. IR: 276.00. VT: 180.00. Líquido: 2304.00
        salario_bruto = 3000.00
        resultado = calcular_salario_liquido(salario_bruto, vale_transporte=True)
        self.assertEqual(resultado, 2304.00)

    def test_v2_completo(self):
        # Salário 5000. INSS: 400.00. BC_IR: 4600.00. IR Bruto: 920.00.
        # Desconto dependente (1): 46.00. IR Final: 874.00. VT: 300.00. Líquido: 3426.00
        salario_bruto = 5000.00
        dependentes = 1
        resultado = calcular_salario_liquido(salario_bruto, dependentes=dependentes, vale_transporte=True)
        self.assertEqual(resultado, 3426.00)

    def test_v2_inss_teto_sem_ir(self):
        # Salário 7000. INSS: 500.00. BC_IR: 6500.00. IR V2 Faixa 3: 1300.00. Líquido: 5200.00
        salario_bruto = 7000.00
        resultado = calcular_salario_liquido(salario_bruto)
        self.assertEqual(resultado, 5200.00)

    

    

if __name__ == "__main__":
    unittest.main(verbosity=2)
