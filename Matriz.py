print('-='*20)
print('{:^40}'.format('Matrizes com Listas'))
print('-='*20)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
Par = Impar = 0
Terceira_Coluna = maior = 0
for linha in range(0,3):
    for colunas in range(0,3):
        matriz[linha][colunas] = int(input(f'Digite um valor para [{linha},{colunas}]: '))
print()
print('-='*20)  
print('MATRIZES:')    
for linha in range(0,3):
    for colunas in range(0,3):
        print(f'[{matriz[linha][colunas]:^4}]',end=' ')  
        if matriz[linha][colunas] % 2 == 0:
            Par += matriz[linha][colunas]
        else:
            Impar += matriz[linha][colunas]
    print()        
print('-='*20)
print(f'A soma dos valores PARES é igual a {Par}')
print(f'A soma dos valores IMPARES é igual a {Impar}')
for linha in range(0,3):
    Terceira_Coluna += matriz[linha][2]
print(f'A SOMA dos valores da TERCEIRA COLUNA é igual a {Terceira_Coluna}')
for colunas in range(0,3):
    if colunas == 0:
        maior = matriz[linha][2]
    elif matriz[linha][2] > maior:
        maior = matriz[linha][2] 
print()        
print(f'O MAIOR VALOR da TERCEIRA COLUNA á o {maior}')
print('-='*20) 







