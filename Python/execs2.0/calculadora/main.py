print('--------------------CALCULADORA PYTHON--------------------')


def soma():
    opcao = int(input('Digite o número da operação que deseja fazer: \n1- ADIÇÃO \n2- SUBTRAÇÃO \n3- MULTIPLICAÇÃO \n4- DIVISÃO: '))
    if opcao == 1:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        result = n1 + n2
        print(f'A soma entre {n1} e {n2} é : {result}')
soma()




