print('-='*30)
print('{:^60}'.format('Listas com Pares e Impares'))
print('-='*32)
numeros = []
pares = []
impares = []
cont = 0
for valores in range(1,8):
    numeros.append(int(input(f'Digite {valores}º valor: ')))
    numeros.sort()
print('-='*30)
for valor in range(0, len(numeros)):
        if numeros[valor] % 2 == 0:
               pares.append(numeros[valor])
        else:
              impares.append(numeros[valor])
print(f'NÚMEROS PARES: {pares}')
print(f'NÚMEROS ÍMPARES: {impares}')
print('')
print(f'Organizados em ORDEM CRESCENTE: {numeros}')
print('-='*30)