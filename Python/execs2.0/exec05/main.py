nome = input('Nome: ')
email = input('E-mail: ')

if nome and email:
    po_a = email.find('@')
    servidor = email[po_a:]
    if po_a != -1 and '.' in servidor:
        print('cadastro concluido')
else:
    print('digite corretamente')