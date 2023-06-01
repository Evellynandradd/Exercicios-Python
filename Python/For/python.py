produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]
tamanho = len(produtos)
for i in range(produtos):
  print('{} unidades produzidas de {}'.format(producao[i], produtos[i]))