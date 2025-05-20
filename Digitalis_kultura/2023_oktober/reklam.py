lst = open('Digitalis_kultura\\2023_oktober\\rendel.txt','r').read().split('\n')
for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
print(lst)

print('2.feladat')

print(f'A rendelesek szama: {len(lst)}')

print('3.feladat')
nap = 9
rendelesek_szama = 0

for i in lst:
    if i[0] == '9':
        rendelesek_szama += 1
        
print(f'A rendelesek szama az adott napon: {rendelesek_szama}')

print('4. feladat')

napok_amior_vettek = []

for i in lst:
    if i[1] == 'NR' and i[0] not in napok_amior_vettek:
        napok_amior_vettek.append(i[0])
        
print(f'{30-len(napok_amior_vettek)} nap nem volt a reklámban nem érintett városból rendelés ')

print('5.feladat')

legtobb = 0
napja = None

for i in lst:
    if int(i[2]) > legtobb:
        legtobb = int(i[2])
        
for i in lst:
    if int(i[2]) == legtobb:
        napja = i[0]
        
print(f'A legnagyobb darabszám: {legtobb}, a rendelés napja: {napja} ')

#print('6.feladat')

def osszes(varos,nap):
    rendelesek = 0
    for i in lst:
        if i[1] == varos and int(i[0]) == nap:
            rendelesek += int(i[2])
    return(rendelesek)
            
print(osszes('NR',15))

print('7.feladat')

print(f'A rendelt termékek darabszáma a 21. napon PL: {osszes('PL',21)} TV: {osszes('TV',21)} NR: {osszes('NR',21)} ')

print('8.feladat')

osszesites = [['PL',0,0,0],['TV',0,0,0],['NR',0,0,0]]

for i in lst:
    if int(i[0]) <= 10:
        if i[1] == 'PL':
            osszesites[0][1] += 1
        if i[1] == 'TV':
            osszesites[1][1] += 1
        if i[1] == 'NR':
            osszesites[2][1] += 1
    if int(i[0]) > 10 and int(i[0]) <= 20:
        if i[1] == 'PL':
            osszesites[0][2] += 1
        if i[1] == 'TV':
            osszesites[1][2] += 1
        if i[1] == 'NR':
            osszesites[2][2] += 1
    if int(i[0]) > 20:
        if i[1] == 'PL':
            osszesites[0][3] += 1
        if i[1] == 'TV':
            osszesites[1][3] += 1
        if i[1] == 'NR':
            osszesites[2][3] += 1
            
print(osszesites)