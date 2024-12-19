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
    cidades = [
        'Berlin', 
        'Tokyo', 
        'Nairobi', 
        'Rio de Janeiro', 
        'Denver', 
        'Moscou', 
        'Helsinki', 
        'Lisboa', 
        'Palermo', 
        'São Paulo', 
        'brasília', 
        'Itabira Minas Gerais',
        'Kabul', 'Tirana', 'Argel', 'Andorra la Vella', 'Luanda', 'Saint John\'s', 'Buenos Aires', 'Yerevan', 'Canberra', 'Viena', 'Baku', 'Nassau', 'Manama', 'Daca', 'Bridgetown', 'Minsk', 'Bruxelas', 'Belmopan', 'Porto-Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasília', 'Bandar Seri Begawan', 'Sófia', 'Ouagadougou', 'Bujumbura', 'Praia', 'Phnom Penh', 'Yaoundé', 'Ottawa', 'Bangui', 'N\'Djamena', 'Santiago', 'Pequim', 'Bogotá', 'Moroni', 'Kinshasa', 'Brazzaville', 'San José', 'Zagreb', 'Havana', 'Nicósia', 'Praga', 'Copenhague', 'Djibouti', 'Roseau', 'Santo Domingo', 'Quito', 'Cairo', 'San Salvador', 'Malabo', 'Asmara', 'Tallinn', 'Addis Abeba', 'Suva', 'Helsinque', 'Paris', 'Libreville', 'Banjul', 'Tbilisi', 'Berlim', 'Acra', 'Atenas', 'Saint George\'s', 'Guatemala', 'Conacri', 'Bissau', 'Georgetown', 'Port-au-Prince', 'Tegucigalpa', 'Budapeste', 'Reykjavik', 'Nova Deli', 'Jacarta', 'Teerã', 'Bagdá', 'Dublin', 'Jerusalém', 'Roma', 'Kingston', 'Tóquio', 'Amã', 'Astana', 'Nairóbi', 'Tarawa', 'Pyongyang', 'Seul', 'Pristina', 'Cidade do Kuwait', 'Bishkek', 'Vientiane', 'Riga', 'Beirute', 'Maseru', 'Monróvia', 'Trípoli', 'Vaduz', 'Vilnius', 'Luxemburgo', 'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Malé', 'Bamako', 'Valeta', 'Majuro', 'Nouakchott', 'Port Louis', 'Cidade do México', 'Palikir', 'Chisinau', 'Mônaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo', 'Windhoek', 'Yaren', 'Katmandu', 'Amsterdã', 'Wellington', 'Manágua', 'Niamey', 'Abuja', 'Oslo', 'Mascate', 'Islamabad', 'Ngerulmud', 'Cidade do Panamá', 'Port Moresby', 'Assunção', 'Lima', 'Manila', 'Varsóvia', 'Lisboa', 'Doha', 'Bucareste', 'Moscou', 'Kigali', 'Basseterre', 'Castries', 'Kingstown', 'Apia', 'San Marino', 'São Tomé', 'Riad', 'Dacar', 'Belgrado', 'Victoria', 'Freetown', 'Cingapura', 'Bratislava', 'Liubliana', 'Honiara', 'Mogadíscio', 'Pretória', 'Juba', 'Madrid', 'Cartum', 'Paramaribo', 'Estocolmo', 'Berna', 'Damasco', 'Taipei', 'Dushanbe', 'Dodoma', 'Bangcoc', 'Lomé', 'Nukualofa', 'Port of Spain', 'Túnis', 'Ancara', 'Ashgabat', 'Funafuti', 'Kampala', 'Kiev', 'Abu Dhabi', 'Londres', 'Washington, D.C.', 'Montevidéu', 'Tashkent', 'Porto Vila', 'Caracas', 'Hanói', 'Lusaka', 'Harare'
    ]
    cidade = ''
    seed = ''
    
    while(len(numbers) < 6):
        cidade = cidades[random.randint(0, len(cidades)-1)]
        seed += str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f%f%f%f%f '))+str(cidade)+' '+str(paraCidade(cidade)) +' '+ str(wheatherapi(cidade))
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

print("salvo em /home/uroot/ws-mega-sena/sorteados.txt")


