print('-='*15)
print('{:^30}'.format('LISTA E ANÁLISE DE DADOS'))
print('-='*15)
cadastro = []
pesados = []
leves = []
opção = 'S'
while opção == 'S':
    nome = str(input('Digite o NOME da pessoa: '))
    peso = float(input('Digite o PESO da pessoa: '))
    cadastro.append([nome, peso])
    print('-='*15)

    opção = str(input('Deseja adicionar outra pessoa? [S/N] ')).upper().strip()[0]
    print('-='*15)

    while opção != 'S' and opção != 'N':
        opção = str(input('Opção Inválida! Deseja adicionar outra pessoa? [S/N] ')).upper().strip()[0]
    print()

print('-='*15)
maior_peso = menor_peso = cadastro[0][1]
for i in range(1, len(cadastro)):
    if cadastro[i][1] > maior_peso:
        maior_peso = cadastro[i][1]
    if cadastro[i][1] < menor_peso:
        menor_peso = cadastro[i][1]

for j in range(0, len(cadastro)):
    if cadastro[j][1] == maior_peso:
        pesados.append(cadastro[j][0])
    if cadastro[j][1] == menor_peso:
        leves.append(cadastro[j][0])

print(f'Foram cadastradas {len(cadastro)} pessoas. ')
print(f'Mais pesados: {pesados} com {maior_peso:.1f}kg ')
print(f'Mais leves: {leves} com {menor_peso:.1f}kg ')
print('-='*15)