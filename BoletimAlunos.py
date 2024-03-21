print('-='*23)
print('{:^46}'.format('BOLETIM ESCOLAR'))
print('-='*23)
bimestre = list()
Aluno = []
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
print('')    
print('-' * 8, 'BOLETIM', '-' * 8)    
print(f'{"Nº":<4}{"ALUNO(A) ":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, aluno in enumerate(bimestre):
   print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8}')
print('-='*23) 
from time import sleep       
while True:
    opcao = int(input('Mostrar notas de Qual Aluno ? (999 interrope): '))
    if opcao == 999:
        print('{:^46}'.format('FINALIZANDO O PROGRAMA...'))
        sleep(2)
        break 
    if opcao <= len(bimestre) - 1:
        print(f'Notas de {bimestre[opcao][0]} são {bimestre[opcao][1]}')
        print('')
        print('-='*23)
print('{:^46}'.format('<<< Volte Sempre >>>'))



