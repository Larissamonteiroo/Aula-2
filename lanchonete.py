from funcoes import soma

lanche = {'cachorro quente': 5.50, 'misto quente': 2.80, 'x-burguer': 8.90, 'x-tudo': 12.00}
bebidas = {'água': 1.00, 'guaraná': 2.50, 'refrigerante lata': 4.00}

print(f'Escolha seu produto')

pedidol = input('Digite seu lanche:')
pedidob = input('Digite sua bebida:')
soma(lanche[pedidol], bebidas[pedidob])


