lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]


for i in range(0,260):	 
	lista.append(28)
	
for i in range(0,264):	
	lista.append(4)
	
for i in range(0,254):	
	lista.append(49)
	
for i in range(0,259):	
	lista.append(35)
	
for i in range(0,237):	
	lista.append(47)
	
for i in range(0,254):	
	lista.append(32)
	
for i in range(0,261):	
	lista.append(30)
	
for i in range(0,237):	
	lista.append(20)
	
for i in range(0,281):	
	lista.append(53)
	
for i in range(0,258):	
	lista.append(44)
	
for i in range(0,234):	
	lista.append(19)

for i in range(0,269):	 
 	lista.append(5)
	
for i in range(0,281):	
	lista.append(53)
	
for i in range(0,233):	
	lista.append(39)
	
for i in range(0,254):	
	lista.append(32)
	
for i in range(0,257):	
	lista.append(17)
	
for i in range(0,254):	
	lista.append(32)
	
for i in range(0,258):	
	lista.append(11)
	
for i in range(0,269):	
	lista.append(42)
	
for i in range(0,280):	
	lista.append(10)
	
for i in range(0,212):	
	lista.append(21)
	
for i in range(0,248):	
	lista.append(8)

for i in range(0,262):	 
 	lista.append(27)
	
for i in range(0,242):	
	lista.append(18)
	
for i in range(0,240):	
	lista.append(58)
	
for i in range(0,250):	
	lista.append(56)
	
for i in range(0,255):	
	lista.append(24)
	
for i in range(0,264):	
	lista.append(4)
	
for i in range(0,269):	
	lista.append(37)
	
for i in range(0,261):	
	lista.append(30)
	
for i in range(0,259):	
	lista.append(34)
	
for i in range(0,263):	
	lista.append(23)
	
for i in range(0,259):	
	lista.append(54)

for i in range(0,269):	 
 	lista.append(37)
	
for i in range(0,257):	
	lista.append(29)
	
for i in range(0,233):	
	lista.append(60)
	
for i in range(0,280):	
	lista.append(10)
	
for i in range(0,281):	
	lista.append(53)
	
for i in range(0,256):	
	lista.append(43)
	
for i in range(0,242):	
	lista.append(18)
	
for i in range(0,260):	
	lista.append(41)
	
for i in range(0,259):	
	lista.append(54)
	
for i in range(0,252):	
	lista.append(36)
	
for i in range(0,260):	
	lista.append(28)

for i in range(0,259):	 
 	lista.append(35)
	
for i in range(0,237):	
	lista.append(45)
	
for i in range(0,258):	
	lista.append(44)
	
for i in range(0,258):	
	lista.append(16)
	
for i in range(0,259):	
	lista.append(34)
	
for i in range(0,247):	
	lista.append(52)
	
for i in range(0,260):	
	lista.append(28)
	
for i in range(0,280):	
	lista.append(10)
	
for i in range(0,237):	
	lista.append(47)
	
for i in range(0,253):	
	lista.append(38)
	
for i in range(0,239):	
	lista.append(12)

for i in range(0,263):	
 	lista.append(23)
	
for i in range(0,265):	
	lista.append(33)
	
for i in range(0,258):	
	lista.append(16)
	
for i in range(0,216):	
	lista.append(22)
	
for i in range(0,261):	
	lista.append(30)
	
for i in range(0,280):	
	lista.append(10)
	
for i in range(0,257):	
	lista.append(17)
	
for i in range(0,269):	
	lista.append(5)
	
for i in range(0,281):	
	lista.append(53)
	
for i in range(0,269):	
	lista.append(42)
	
for i in range(0,234):	
	lista.append(57)


with open('toplistNumerosSorteados.txt', 'w') as file:
    file.write("toplist = [")
    for numero in lista:
        file.write(str(numero)+",")
    file.write("]")



