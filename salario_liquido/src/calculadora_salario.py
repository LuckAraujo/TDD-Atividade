def validar_salario(salario_bruto: float) -> None:
    if salario_bruto <= 0:
        raise ValueError("Salário bruto deve ser maior que zero")


def calcular_inss(salario_bruto: float) -> float:
    desconto = salario_bruto * 0.08
    return min(desconto, 500.0)


def calcular_irrf(salario_bruto: float) -> float:
    if salario_bruto <= 2000:
        return 0.0
    return salario_bruto * 0.10


def calcular_salario_liquido(salario_bruto: float) -> float:
    validar_salario(salario_bruto)

    desconto_inss = calcular_inss(salario_bruto)
    desconto_irrf = calcular_irrf(salario_bruto)

    salario_liquido = salario_bruto - desconto_inss - desconto_irrf

    return round(salario_liquido, 2)
