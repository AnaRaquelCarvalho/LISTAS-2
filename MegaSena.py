print('-='*23)
print('{:^46}'.format('JOGA NA MEGA SENA - PALPITES'))
print('-='*23)
from random import randint
from time import sleep
jogador = list()
jogos = list()
numeros = int(input(f'Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= numeros:
    cont = 0
    while True:
        computador = randint(1,60)
        if computador not in jogador:
            jogador.append(computador)
            cont += 1
        if cont >= 6:
            break
    jogador.sort()
    jogos.append(jogador[:])
    jogador.clear()
    tot += 1
sleep(1)
print('-='*6, f' SORTEANDO {numeros} JOGOS ','-='*6)
for jogos, jogador in enumerate (jogos):
         print(f'Jogo {jogos}: {jogador}')
sleep(1)
print('-='*6, '< BOA SORTE! >', '-='*6)      


 
