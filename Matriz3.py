print('-='*20)
print('{:^40}'.format('Matrizes com Listas 3'))
print('-='*20)
matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para [{linhas},{colunas}]: '))
print()
print('-='*20)  
print('MATRIZES:')         
for linhas in range(0, 4):
    for colunas in range(0, 6):
        print(f'[{matriz[linhas][colunas]:^4}]',end=' ')    
    print()        
print('-='*20)

