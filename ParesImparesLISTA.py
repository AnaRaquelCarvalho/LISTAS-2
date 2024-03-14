print('-='*30)
print('{:^60}'.format('Listas 2 com Pares e Impares'))
print('-='*30)
numeros = [[], []]
valor = 0
for valores in range(1,8):
    valor = int(input(f'Digite {valores}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-='*30)
numeros[0].sort()
numeros[1].sort()
print(f'Números pares Digitados: {numeros[0]}')
print(f'Números Ímpares Digitados: {numeros[1]}')
print()
print(f'Organizados em ORDEM CRESCENTE: {numeros}')
print('-='*30)
