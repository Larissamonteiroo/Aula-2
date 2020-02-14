
sanduiches = ('cachorro quente', 'misto quente', 'x-burguer', 'x-tudo', 'x-salada')
sanduichesPreco = (4.5, 3, 8.9, 12, 5.5)

bebidas = ('água', 'guaraná', 'refri lata', 'suco natural')
bebidasPreco = (1, 2.5, 4, 3.5)

cont = 1
print('------ Nossos sanduiches ------')
for x in sanduiches:
    print(f'{cont} - {x} -> {sanduichesPreco[cont-1]}')
    cont += 1

print('')
print('---------- Bebidas ----------')

cont = 0
while ( cont <= len(bebidas)-1 ):
    print(f'{cont+1} - {bebidas[cont]} -> {bebidasPreco[cont]}')
    cont += 1

compraSanduiche = int(input('Informe o sanduiche: '))
compraBebida = int(input('Informe a bebida: '))

total = sanduichesPreco[ compraSanduiche-1 ] + bebidasPreco[ compraBebida-1 ]

print(f'Total a pagar: R$ {total:.2f}')
