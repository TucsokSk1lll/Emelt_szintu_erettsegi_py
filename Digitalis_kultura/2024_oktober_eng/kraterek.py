import math
lst = open('Digitalis_kultura\\2024_oktober_eng\\felszin_tpont.txt','r').read().split('\n')

#print(lst)

for i in range(len(lst)):
    lst[i] = lst[i].split('\t')

#print(lst)

dict = {}

for i in range(len(lst)):
    dict.update({lst[i][3]:{'x':float(lst[i][0]),'y':float(lst[i][1]),'kozeppont':float(lst[i][2])}})
                
print(dict)

print('2.feladat')

print(f'A kraterek szama: {len(dict)}')

print('3.feladat')

nev = 'Thomas Gold'
print(f"A(z) {nev} középpontja X={dict[nev]['x']} Y={dict[nev]['y']} sugara R={dict[nev]['kozeppont']}.")

print('4.feladat')
legnagyob = 'George Ogden Abell'
for i in dict:
    if dict[i]['kozeppont'] > dict[legnagyob]['kozeppont']:
        legnagyob = i

print(f"A legnagyobb kráter neve és sugara: {legnagyob} {dict[legnagyob]['kozeppont']}")

#print('5.feladat')

def tavolsag(x1,y1,x2,y2):
    tavolsag = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    return tavolsag

print('6.feladat')

nev2 = 'Jacques Cassini'

print('Nincs kozos resze: ',end='')
for i in dict:
    if tavolsag(dict[nev2]['x'],dict[nev2]['y'],dict[i]['x'],dict[i]['y']) > dict[nev2]['kozeppont'] + dict[i]['kozeppont']:
        print(f'{i}',end=', ')

print('7.feladat')

for i in dict:
    if tavolsag(dict[nev2]['x'],dict[nev2]['y'],dict[i]['x'],dict[i]['y']) > abs(dict[nev2]['kozeppont'] - dict[i]['kozeppont']):
        print(f'{i}',end=', ')