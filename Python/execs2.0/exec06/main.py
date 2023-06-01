meses = ['jan', 'fev', 'mar', 'abr', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19000]
vendas_2sem = [1958, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)

maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)

i_maior_valor = vendas_1sem.index(maior_valor)
i_menor_valor = vendas_1sem.index(maior_valor)

print('O melhor mês do ano foi {} com {} vendas'.format(meses[i_maior_valor], maior_valor))
print('O pior mês do ano foi {} com {} vendas'.format(meses[i_menor_valor],menor_valor))

fat_total = sum(vendas_1sem)
print('fat total: {} '.format(fat_total)) 


top3 = []
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
print(top3)
print(vendas_1sem)
