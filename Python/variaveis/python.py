nome = input('DIGITE SEU NOME: ')
idade = int(input('DIGITE SUA IDADE: '))
anoNasc = 2023 - idade
maior = idade > 18
altura = 1.64
peso = 54
imc = peso / altura ** 2
print(nome, 'Você naceu em', anoNasc)
print(nome, 'seu imc é', int(imc))