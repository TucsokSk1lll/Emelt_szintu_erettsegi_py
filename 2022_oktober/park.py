lst = open('2022_oktober\\felajanlas.txt','r').read().split('\n')
agyasok = None
for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
agyasok = lst[0]
lst.pop(0)
print(lst)

print('2.feladat')

print(f'A felajanlasok szama: {len(lst)}')

print('3.feladat')

text = 'A bejarat mindket oldalara ultetok:'

for i in range(len(lst)):
    if int(lst[i][0]) > int(lst[i][1]):
        text += f' {i+1}'
    
print(text)

print('4. feladat')

sorszam = 100
darab = 0
szin = None
viragok = []

for i in lst:
    if (int(i[0]) <= sorszam and int(i[1]) >= sorszam) or (int(i[0]) >= sorszam and int(i[1]) >= sorszam and int(i[0]) > int(i[1])):
        print(i)
        darab += 1
        if szin == None:
            szin = i[2]
        if i[2] not in viragok:
            viragok.append(i[2])

print(f'A felajanlok szama: {darab}')
if darab == 0:
    print('Ezt az ágyást nem ültetik be.')
else:
    print(f'A virágágyás színe, ha csak az első ültet: {szin}')

print(f'A virágágyás színei: {viragok}')

print('5.feladat')

ultetes = []

for i in range(int(agyasok[0])):
    ultetes.append(0)

for i in range(len(lst)):
    if int(lst[i][0]) <= int(lst[i][1]):
        for j in range(int(lst[i][0]),int(lst[i][1])):
            if ultetes[j] == 0:
                ultetes[j] = [lst[i][2],i+1]
    else:
        for j in range(int(lst[i][0]),int(agyasok[0])):
            if ultetes[j] == 0:
                ultetes[j] = [lst[i][2],i+1]
        for j in range(0,int(lst[i][1])+1):
            if ultetes[j] == 0:
                ultetes[j] = [lst[i][2],i+1]
print(ultetes)

beultetett = 0
felajanlasok_szama = 0

for i in ultetes:
    if i !=0 :
        beultetett += 1
for i in lst:
    if int(i[0]) <= int(i[1]):
        felajanlasok_szama += int(i[1])-int(i[0])+1
    else:
        felajanlasok_szama += int(agyasok[0])-int(i[0])
        felajanlasok_szama += int(i[1])+1

print(felajanlasok_szama)
print(beultetett)



if 0 not in ultetes:
    print('Minden ágyás beültetésére van jelentkező.')
elif felajanlasok_szama > beultetett:
    print('Átszervezéssel megoldható a beültetés.')
elif beultetett > felajanlasok_szama:
    print('A beültetés nem oldható meg.')

#print('6.feladat')

file = open('2022_oktober\\szinek.txt','w')
for i in ultetes:
    if i != 0:
        file.write(f'{i[0]} {i[1]}\n')
    else:
        file.write(f'# 0\n')