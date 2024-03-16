print('-='*20)
print('{:^40}'.format('Matrizes com Listas 2'))
print('-='*20)
matriz = [[],[],[]]
for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*20)
print('MATRIZES ')
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
print('-='*20)        