import unittest

from src.calculadora_salario import calcular_salario_liquido


class TestCompatibilidadeV1(unittest.TestCase):

    def test_v1_salario_ate_2000_sem_parametros_novos(self):
        print("\n[TESTE RED] V2 - salário até 2000 sem novos parâmetros")

        salario_bruto = 2000.00
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = salario_bruto * 0.08
        esperado = salario_bruto - desconto_inss

        print(f"Desconto INSS: {desconto_inss}")
        print(f"Resultado esperado (V2): {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))

    def test_v1_salario_acima_2000_com_irrf(self):
        print("\n[TESTE RED] V2 - salário acima de 2000 sem novos parâmetros")

        salario_bruto = 3000.00
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = salario_bruto * 0.08
        desconto_irrf = salario_bruto * 0.10
        esperado = salario_bruto - desconto_inss - desconto_irrf

        print(f"Desconto INSS: {desconto_inss}")
        print(f"Desconto IRRF: {desconto_irrf}")
        print(f"Resultado esperado (V1): {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))

    def test_v1_inss_deve_respeitar_teto(self):
        print("\n[TESTE RED] V2 - INSS com teto sem novos parâmetros")

        salario_bruto = 10000.00
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = 500.00
        desconto_irrf = salario_bruto * 0.10
        esperado = salario_bruto - desconto_inss - desconto_irrf

        print(f"Desconto INSS (teto): {desconto_inss}")
        print(f"Desconto IRRF: {desconto_irrf}")
        print(f"Resultado esperado (V2): {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))

    def test_v1_nao_deve_aplicar_vale_transporte_por_padrao(self):
        print("\n[TESTE RED] V2 - não deve aplicar vale-transporte por padrão")

        salario_bruto = 3000.00
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = salario_bruto * 0.08
        desconto_irrf = salario_bruto * 0.10
        esperado = salario_bruto - desconto_inss - desconto_irrf

        print("Vale-transporte não informado → desconto 0")
        print(f"Resultado esperado (V1): {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))

    def test_v1_dependentes_padrao_zero(self):
        print("\n[TESTE RED] V2 - dependentes padrão devem ser zero")

        salario_bruto = 3000.00
        print(f"Salário bruto: {salario_bruto}")

        resultado = calcular_salario_liquido(salario_bruto)

        desconto_inss = salario_bruto * 0.08
        desconto_irrf = salario_bruto * 0.10
        esperado = salario_bruto - desconto_inss - desconto_irrf

        print("Dependentes não informados → 0 dependentes")
        print(f"Resultado esperado (V2): {round(esperado, 2)}")
        print(f"Resultado obtido: {resultado}")

        self.assertEqual(resultado, round(esperado, 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
