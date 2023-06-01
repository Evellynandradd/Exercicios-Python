def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    valorhora = float(valor_hora)

    if horas <= 40:
        salario = valorhora * horas
    else:
        extra = horas - 40
        salario = (40 * valorhora) + ((extra * 1.5) * valorhora)
        return salario



from main import calcular_pagamento

horas_trab = float(input('digite as horas trabalhadas: '))
valor_hora = float(input('digite o valor pago: '))

total_salario = calcular_pagamento (horas_trab, valor_hora)
print('o valor do salario é de : , total_salario')



