from funcoes import soma

lanches = [('cachorro quente', 5.50), ('misto quente', 2.80), ('x-burguer', 8.90), ('x-tudo', 12.00)]
bebidas = {'água': 1.00, 'guaraná': 2.50, 'refrigerante lata': 4.00}

cont = 1
print('------> Nossos Lanches <------')
for precol in lanches:
    print(f'{cont} - {lanches}')
    cont += 1

contg = 1
print('---------> Bebidas <---------')
for precob in bebidas:
    print(f'{contg} - {precob} -> R$ {bebidas[precob]}')
    contg += 1

print(f'Escolha seu produto')

pedidol = int(input('Digite seu lanche:'))
pedidob = int(input('Digite sua bebida:'))
total = precol[pedidol-1] + precob[pedidob-1]

print(f'Total a pagar: R$ {total}')


