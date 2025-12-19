# =====================
# Constantes de domínio
# =====================
ALIQUOTA_INSS = 0.08
TETO_INSS = 500.00

ALIQUOTA_IR_FAIXA_1 = 0.00
ALIQUOTA_IR_FAIXA_2 = 0.10
ALIQUOTA_IR_FAIXA_3 = 0.20

ALIQUOTA_VALE_TRANSPORTE = 0.06
ALIQUOTA_DEPENDENTE_IR = 0.05


# =====================
# Funções auxiliares
# =====================
def _validar_salario(salario_bruto: float) -> None:
    if salario_bruto <= 0:
        raise ValueError("Salário bruto deve ser maior que zero")


def _validar_dependentes(dependentes: int) -> None:
    if dependentes < 0:
        raise ValueError("Número de dependentes não pode ser negativo")


def _calcular_inss(salario_bruto: float) -> float:
    desconto = salario_bruto * ALIQUOTA_INSS
    return min(desconto, TETO_INSS)


def _calcular_ir_v1(salario_bruto: float) -> float:
    return salario_bruto * ALIQUOTA_IR_FAIXA_2 if salario_bruto > 2000 else 0.0


def _calcular_ir_bruto_v2(salario_bruto: float) -> float:
    if salario_bruto <= 2000:
        return salario_bruto * ALIQUOTA_IR_FAIXA_1
    if salario_bruto <= 4000:
        return salario_bruto * ALIQUOTA_IR_FAIXA_2
    return salario_bruto * ALIQUOTA_IR_FAIXA_3


def _aplicar_desconto_dependentes(ir: float, dependentes: int) -> float:
    desconto = ir * (ALIQUOTA_DEPENDENTE_IR * dependentes)
    return max(ir - desconto, 0.0)


def _calcular_vale_transporte(salario_bruto: float, vale_transporte: bool) -> float:
    return salario_bruto * ALIQUOTA_VALE_TRANSPORTE if vale_transporte else 0.0


# =====================
# Função principal
# =====================
def calcular_salario_liquido(salario_bruto, *args) -> float:
    """
    V1: calcular_salario_liquido(salario_bruto)
    V2: calcular_salario_liquido(salario_bruto, dependentes, vale_transporte)
    """

    _validar_salario(salario_bruto)

    desconto_inss = _calcular_inss(salario_bruto)

    # =====================
    # MODO V1
    # =====================
    if len(args) == 0:
        desconto_ir = _calcular_ir_v1(salario_bruto)
        return round(
            salario_bruto - desconto_inss - desconto_ir,
            2
        )

    # =====================
    # MODO V2
    # =====================
    dependentes, vale_transporte = args
    _validar_dependentes(dependentes)

    ir_bruto = _calcular_ir_bruto_v2(salario_bruto)
    ir_final = _aplicar_desconto_dependentes(ir_bruto, dependentes)
    desconto_vale = _calcular_vale_transporte(salario_bruto, vale_transporte)

    salario_liquido = (
        salario_bruto
        - desconto_inss
        - ir_final
        - desconto_vale
    )

    return round(salario_liquido, 2)
