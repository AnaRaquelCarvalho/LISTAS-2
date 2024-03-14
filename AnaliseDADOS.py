print('-='*15)
print('{:^30}'.format('LISTA E ANÁLISE DE DADOS'))
print('-='*15)
nome = []
pessoas = []
peso = list()
while True:     
    nome.append(str(input('Nome: ')))    
    ps = float(input('Peso: '))
    peso.append(ps)   
    nome.append(ps)
    pessoas.append(nome[:])    
    nome.clear()    
    print('-='*15)
    resposta = str(input('\nQuer continuar? [S/N]  ')).strip().upper()[0]
    if resposta in 'nN':
        break    
    print('')
    print('-='*15)
maior = max(peso)
menor = min(peso)
print('\nTotal de pessoas cadastradas: {}'.format(len(pessoas)))
print('\nMaior peso: {}. É o peso de:'.format(maior), end = ' ')
for p in pessoas:
    if p[1] == maior:
        print('[{}] '.format(p[0]),end = '')
print('\nMenor peso: {}. É o peso de:'.format(menor), end = ' ')
for p in pessoas:
    if menor == p[1]:
        print('[{}] '.format(p[0]), end = '')
print('\n','-='*15)        
 
