import random
from datetime import datetime
from testeClimate import *


def aposta():
    
    numbers = []
    cidades = ['Berlin', 'Tokyo', 'Nairobi', 'Rio de Janeiro', 'Denver', 'Moscou', 'Helsinki', 'Lisboa', 'Palermo']
    cidade = ''
    seed = ''

    while(len(numbers) < 6):
        cidade = cidades[random.randint(0, len(cidades)-1)]
        seed += str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f%f%f%f%f '))+str(cidade)+' '+str(paraCidade(cidade))
        random.seed(seed)
        number = random.randint(1,60)
        if number not in numbers:
            numbers.append(number)
            
    numbers.sort()
    print(numbers)
    numbers.clear()

for x in range(4):
    aposta()
