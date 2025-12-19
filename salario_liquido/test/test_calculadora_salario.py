import unittest

from src.calculadora_salario import calcular_salario_liquido


class TestCalculadoraSalario(unittest.TestCase):

    def test_salario_ate_2000_isento_de_irrf(self):
        salario_bruto = 2000.00
        print("\n[TESTE] Salário até 2000 (isento de IRRF)")
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = salario_bruto * 0.08
        esperado = salario_bruto - desconto_inss

        print(f"Desconto INSS: {desconto_inss}")
        print(f"Resultado esperado: {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))

    def test_salario_acima_2000_com_irrf(self):
        salario_bruto = 3000.00
        print("\n[TESTE] Salário acima de 2000 (com IRRF)")
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = salario_bruto * 0.08
        desconto_irrf = salario_bruto * 0.10
        esperado = salario_bruto - desconto_inss - desconto_irrf

        print(f"Desconto INSS: {desconto_inss}")
        print(f"Desconto IRRF: {desconto_irrf}")
        print(f"Resultado esperado: {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))

    def test_inss_nao_deve_ultrapassar_teto(self):
        salario_bruto = 10000.00
        print("\n[TESTE] INSS com teto máximo")
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = 500.00
        desconto_irrf = salario_bruto * 0.10
        esperado = salario_bruto - desconto_inss - desconto_irrf

        print(f"Desconto INSS (teto): {desconto_inss}")
        print(f"Desconto IRRF: {desconto_irrf}")
        print(f"Resultado esperado: {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))

    def test_salario_zero_deve_gerar_erro(self):
        salario_bruto = 0
        print("\n[TESTE] Salário zero deve gerar erro")
        print(f"Salário bruto: {salario_bruto}")

        with self.assertRaises(ValueError):
            calcular_salario_liquido(salario_bruto)

        print("Exceção ValueError lançada corretamente")

    def test_salario_negativo_deve_gerar_erro(self):
        salario_bruto = -100
        print("\n[TESTE] Salário negativo deve gerar erro")
        print(f"Salário bruto: {salario_bruto}")

        with self.assertRaises(ValueError):
            calcular_salario_liquido(salario_bruto)

        print("Exceção ValueError lançada corretamente")

    def test_resultado_deve_ter_duas_casas_decimais(self):
        salario_bruto = 1234.567
        print("\n[TESTE] Arredondamento para duas casas decimais")
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        print(f"Resultado obtido: {resultado}")
        print(f"Resultado arredondado esperado: {round(resultado, 2)}")

        self.assertEqual(resultado, round(resultado, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
