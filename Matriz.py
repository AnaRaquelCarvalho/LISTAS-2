print('-='*20)
print('{:^40}'.format('Matrizes com Listas'))
print('-='*20)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for linha in range(0,3):
    for colunas in range(0,3):
        matriz[linha][colunas] = int(input(f'Digite um valor para [{linha},{colunas}]: '))
print()
print('-='*20)  
print('MATRIZES:')    
for linha in range(0,3):
    for colunas in range(0,3):
        print(f'[{matriz[linha][colunas]:^4}]',end=' ')    
    print()        
print('-='*20)
