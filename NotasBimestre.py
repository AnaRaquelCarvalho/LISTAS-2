print('-='*23)
print('{:^46}'.format('NOTAS ESCOLARES'))
print('-='*23)
lista = []
cont = 0
while True:
    lista.append([])
    lista[cont].append(str(input('Digite o nome do aluno: ')))
    lista[cont].append(float(input('Digite a nota do 1º Bimestre: ')))
    lista[cont].append(float(input('Digite a nota do 2º Bimestre: ')))
    lista[cont].append(float(input('Digite a nota do 3º Bimestre: ')))
    lista[cont].append(float(input('Digite a nota do 4º Bimestre: ')))
    media = (lista[cont][1] + lista[cont][2] + lista[cont][3] + lista[cont][4]) / 2
    lista[cont].append(media)
    print('-='*23)
    parar = str(input('Deseja continuar? [S/N] '))
    print('-='*23)
    if parar in 'Nn':
        break
    cont += 1
print('Nº   Aluno          Média')
print('-='*23)
for pos, alun in enumerate(lista):
    print(pos, f'{alun[0]:<15}', alun[5])
while True:
    print('-='*23)
    aluno = int(input('Deseja ver a nota de qual aluno? (999 para parar) '))
    if aluno == 999:
        break
    else:
        print(f'As notas de {lista[aluno][0]} são {lista[aluno][1:5]}')
print('Programa Finalizado\nVolte sempre! :D')
print('-='*23)