def calcular_salario_liquido(salario_bruto, *args):
    """
    V1: calcular_salario_liquido(salario_bruto)
    V2: calcular_salario_liquido(salario_bruto, dependentes, vale_transporte)
    """

    # =====================
    # Validações
    # =====================
    if salario_bruto <= 0:
        raise ValueError("Salário bruto deve ser maior que zero")

    # =====================
    # INSS (V1 e V2)
    # =====================
    desconto_inss = salario_bruto * 0.08
    if desconto_inss > 500:
        desconto_inss = 500.0

    # =====================
    # MODO V1 (compatibilidade total)
    # =====================
    if len(args) == 0:
        desconto_ir = salario_bruto * 0.10 if salario_bruto > 2000 else 0.0

        salario_liquido = salario_bruto - desconto_inss - desconto_ir
        return round(salario_liquido, 2)

    # =====================
    # MODO V2
    # =====================
    dependentes = args[0]
    vale_transporte = args[1]

    if dependentes < 0:
        raise ValueError("Número de dependentes não pode ser negativo")

    # IR progressivo
    if salario_bruto <= 2000:
        desconto_ir = 0.0
    elif salario_bruto <= 4000:
        desconto_ir = salario_bruto * 0.10
    else:
        desconto_ir = salario_bruto * 0.20

    # Dependentes: 5% de abatimento por dependente
    desconto_ir -= desconto_ir * (0.05 * dependentes)
    if desconto_ir < 0:
        desconto_ir = 0.0

    # Vale-transporte: 6%
    desconto_vale = salario_bruto * 0.06 if vale_transporte else 0.0

    salario_liquido = (
        salario_bruto
        - desconto_inss
        - desconto_ir
        - desconto_vale
    )

    return round(salario_liquido, 2)
