x = open(file='Baksa_version\\nevek.txt',mode='r').read().split('\n')
#print(x)

lst = []

for i in range(len(x)):
    lst.append(x[i].split(' '))

#print(lst)

print('2.feladat')
print('A nyilvantartasban ' + str(len(lst)) + ' diak szerepel.')

print('3.feladat')
evfolyam = input('Evfolyam: ')
osztaly = input('Osztaly: ')

for i in range(len(lst)):
    if lst[i][0] == evfolyam and lst[i][1] == osztaly:
        print(lst[i][2]+' '+lst[i][3])

print('4.feladat')
evfolyamok = ['a','b','c','d','e']
letszam = [0,0,0,0,0]

for i in range(len(lst)):
    for j in range(len(evfolyamok)):
        if lst[i][1] == evfolyamok[j]:
            letszam[j] += 1

for i in range(len(evfolyamok)):
    print(evfolyamok[i]+': '+str(letszam[i]))

# 5.feladat
keresztnevek = []

for i in range(len(lst)):
    keresztnevek.append(lst[i][2])

keresztnevek.sort()

#print(keresztnevek)

lista = open(file='Baksa_version\\keresztnevek.txt',mode='w')

for i in range(len(keresztnevek)):
    lista.write(keresztnevek[i]+'\n')