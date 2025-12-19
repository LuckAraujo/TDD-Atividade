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
    """Garante que o salário bruto seja um valor positivo."""
    if salario_bruto <= 0:
        raise ValueError("Salário bruto deve ser maior que zero")


def _validar_dependentes(dependentes: int) -> None:
    """Garante que o número de dependentes não seja negativo."""
    if dependentes < 0:
        raise ValueError("Número de dependentes não pode ser negativo")


def _calcular_inss(salario_bruto: float) -> float:
    """Calcula o desconto do INSS, respeitando o teto máximo."""
    desconto = salario_bruto * ALIQUOTA_INSS
    return min(desconto, TETO_INSS)


def _calcular_ir_v1(base_calculo_ir: float) -> float:
    """Calcula o IR conforme a regra da V1 (10% acima de 2000) sobre a base de cálculo."""
    return base_calculo_ir * ALIQUOTA_IR_FAIXA_2 if base_calculo_ir > 2000 else 0.0


def _calcular_ir_bruto_v2(base_calculo_ir: float) -> float:
    """Calcula o IR bruto conforme as faixas da V2 sobre a base de cálculo."""
    if base_calculo_ir <= 2000:
        return base_calculo_ir * ALIQUOTA_IR_FAIXA_1
    if base_calculo_ir <= 4000:
        return base_calculo_ir * ALIQUOTA_IR_FAIXA_2
    return base_calculo_ir * ALIQUOTA_IR_FAIXA_3


def _aplicar_desconto_dependentes(ir_bruto: float, dependentes: int) -> float:
    """Aplica o desconto de IR por dependente, garantindo que o IR final não seja negativo."""
    desconto = ir_bruto * (ALIQUOTA_DEPENDENTE_IR * dependentes)
    return max(ir_bruto - desconto, 0.0)


def _calcular_vale_transporte(salario_bruto: float, vale_transporte: bool) -> float:
    """Calcula o desconto de vale-transporte se a opção estiver ativada."""
    return salario_bruto * ALIQUOTA_VALE_TRANSPORTE if vale_transporte else 0.0


# =====================
# Função principal refatorada
# =====================
def calcular_salario_liquido(
    salario_bruto: float,
    dependentes: int = 0,
    vale_transporte: bool = False,
    modo_v1: bool = False
) -> float:
    """
    Calcula o salário líquido aplicando descontos de INSS, IR e Vale-Transporte.

    Parâmetros:
    - salario_bruto (float): O salário base.
    - dependentes (int): Número de dependentes para desconto de IR (padrão 0).
    - vale_transporte (bool): Indica se o desconto de vale-transporte deve ser aplicado (padrão False).
    - modo_v1 (bool): Se True, usa a regra de cálculo de IR da V1 (para compatibilidade).

    Retorna:
    - float: O valor do salário líquido, arredondado para duas casas decimais.
    """

    _validar_salario(salario_bruto)
    _validar_dependentes(dependentes)

    desconto_inss = _calcular_inss(salario_bruto)
    base_calculo_ir = salario_bruto - desconto_inss

    if modo_v1:
        # Modo V1: Usa a regra de IR antiga e ignora dependentes/vale-transporte
        desconto_ir = _calcular_ir_v1(base_calculo_ir)
        desconto_total = desconto_inss + desconto_ir
    else:
        # Modo V2 (Padrão): Usa as novas regras de IR, dependentes e vale-transporte
        ir_bruto = _calcular_ir_bruto_v2(base_calculo_ir)
        desconto_ir = _aplicar_desconto_dependentes(ir_bruto, dependentes)
        desconto_vale = _calcular_vale_transporte(salario_bruto, vale_transporte)
        desconto_total = desconto_inss + desconto_ir + desconto_vale

    salario_liquido = salario_bruto - desconto_total

    return round(salario_liquido, 2)
