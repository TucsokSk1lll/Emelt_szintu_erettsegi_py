lst = open('2016_majus\\penztar.txt','r').read().split('\n')
lst2 = [[]]

for i in range(len(lst)):
    if lst[i] != 'F':
        lst2[-1].append(lst[i])
    else:
        lst2.append([])
lst2.pop()
print(lst2)

print('2.feladat')

print(f'A fizetések száma: {len(lst2)}')

print('3.feladat')

print(f'Az első vásárló {len(lst2[0])} darab árucikket vásárolt. ')

#print('4.feladat')
sorszam = 3
arucikk = 'kefe'
darab = 2

print('5.feladat')
elso = 0
utolso = 0
tartalmazza = 0
for i in range(len(lst2)):
    if arucikk in lst2[i]:
        elso = i+1
        break

for i in reversed(range(len(lst2))):
    if arucikk in lst2[i]:
        utolso = i+1
        break

for i in lst2:
    if arucikk in i:
        tartalmazza +=1

print(f'Az első vásárlás sorszáma: {elso} ')
print(f'Az utolsó vásárlás sorszáma: {utolso} ')
print(f'{tartalmazza} vásárlás során vettek belőle. ')

print('6.feladat')

def ertek(darab):
    ar = 0

    if darab != 0:
        ar += 500
        darab -=1

    if darab != 0:
        ar += 450
        darab-=1

    for i in range(darab):
        ar += 400
    
    return(ar)

print(ertek(darab))

print('7.feladat')

aruk = []

for i in range(len(lst2)):
    aru = []
    darab = []
    for j in range(len(lst2[i])):
        if lst2[i][j] not in aru:
            aru.append(lst2[i][j])
            darab.append(1)
        else:
            for k in range(len(aru)):
                if aru[k] == lst2[i][j]:
                    darab[k] += 1
    aruk.append([])
    for i in range(len(aru)):
        aruk[-1].append([aru[i],darab[i]])

print(aruk[1])


#print('8.feladat')

file = open('2016_majus\\osszeg.txt','w')

for i in range(len(aruk)):
    ar = 0
    for j in range(len(aruk[i])):
        ar += ertek(aruk[i][j][1])
    #print(f'{i+1}: {ar}')
    file.write(f'{i+1}: {ar}\n')