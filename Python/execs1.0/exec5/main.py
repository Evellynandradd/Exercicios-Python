km = int(input('Quantidade de Km pecorrido: '))
dias = int(input('Quantos dias: '))

valorkm = 0.15
valordia = 60

pagar = ((km * valorkm) + (valordia * dias))
print(pagar)