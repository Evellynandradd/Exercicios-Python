def par(i):
    if i % 2 == 0:
        return i
    
lista = [1, 3, 3, 4, 5]

lista_par = filter(par, lista)
print(list(lista_par))