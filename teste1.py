alunos = ('Alessan', 'João', 'Maria')
#print alunos[2]

#uso de if / while
#uso do for

'''
for x in alunos:
    print(x)
'''

#atividade - listar todos os itens da lista de frutas abaixo, exceto a uva
frutas = ('Bnana', 'maçã', 'uva', 'pera', 'uva', 'amora')
for f in frutas:
    if f != 'uva':
        continue
        #break
    else:
        print(f)

