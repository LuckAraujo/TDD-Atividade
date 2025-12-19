def calcular_salario_liquido(salario_bruto: float) -> float:
    if salario_bruto <= 0:
        raise ValueError("Salário bruto deve ser maior que zero")

    # Desconto INSS: 8% com teto de 500
    desconto_inss = salario_bruto * 0.08
    if desconto_inss > 500:
        desconto_inss = 500.0

    # Desconto IRRF
    desconto_irrf = 0.0
    if salario_bruto > 2000:
        desconto_irrf = salario_bruto * 0.10

    salario_liquido = salario_bruto - desconto_inss - desconto_irrf

    return round(salario_liquido, 2)
