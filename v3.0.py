import random
from datetime import datetime
from testeClimate import *
from lista import *
from jogos import *

jogos = []
toplist1 = list(toplist)
listaTodosJogos1 = list(listaTodosJogos)

def aposta():

    numbers = []
    cidades = ['Berlin', 'Tokyo', 'Nairobi', 'Rio de Janeiro', 'Denver', 'Moscou', 'Helsinki', 'Lisboa', 'Palermo']
    cidade = ''
    seed = ''
    
    while(len(numbers) < 6):
        cidade = cidades[random.randint(0, len(cidades)-1)]
        seed += str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f%f%f%f%f '))+str(cidade)+' '+str(paraCidade(cidade))
        random.seed(seed)
        number = random.choice(toplist)
        if number not in numbers:
            numbers.append(number)
        if len(numbers) == 6:
            numbers.sort()
            if tuple(numbers) not in listaTodosJogos1:
                jogos.append((numbers))
                listaTodosJogos1.append(tuple(numbers))
                #print(listaTodosJogos1)
            else:
                number = []


for i in range(0,2):
    aposta()

with open('sorteados.txt', 'w') as file:
    for jogo in jogos:
        #print(jogo)
        file.write(str(jogo))
        file.write('\n')


