print('-='*23)
print('{:^46}'.format('JOGANDO NA MEGA SENA - PALPITES'))
print('-='*23)
from time import sleep
from random import randint
jogo = list()
quant = int(input('Quer gerar quantos jogos? '))
print()
resp = ' '
print('-='*23)
for j in range(0, quant):
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    print(f'Jogo {j+1}: {sorted(jogo)}')
    sleep(.5)
    jogo.clear()
print('-='*23)
