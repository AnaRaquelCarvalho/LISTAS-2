print('-='*23)
print('{:^46}'.format('BOLETIM ESCOLAR'))
print('-='*23)
from time import sleep
bimestre = list()
while True:
    Aluno = str(input('Aluno(a): '))
    nota1 = float(input(f'Notas do 1º Bimestre:  '))
    nota2 = float(input(f'Notas do 2º Bimestre:  '))
    nota3 = float(input(f'Notas do 3º Bimestre:  '))
    nota4 = float(input(f'Notas do 4º Bimestre:  '))
    media = (nota1 + nota2 + nota3 + nota4)/4
    bimestre.append([Aluno, [nota1, nota2, nota3, nota4], media])
    print('-='*23) 
    resp = str(input('Quer Continuar adicionando Notas dos alunos? [S/N]: '))
    print('-='*23)  
    if resp in 'Nn':
        break
print(f'{"Nº":<6} {"ALUNO(A)":<6} {"MÉDIA":>10}')
print('-='*23)
for i, a in enumerate(bimestre):
    print(f'{i:<7}{a[Aluno]:<7}{a[media]:>9.1f}')
while True:
    print('-='*23)
    opcao = int(input('Mostrar notas de Qual Aluno ? (999 interrope): '))
    if opcao == 999:
        print('{:^46}'.format('FINALIZANDO O PROGRAMA...'))
    sleep(2)
    break 
if opcao <= len(bimestre) - 1:
        print(f'Notas de {bimestre[opcao][Aluno]} são {bimestre[opcao][media]}')
print('{:^46}'.format('<<< Volte Sempre >>>'))



