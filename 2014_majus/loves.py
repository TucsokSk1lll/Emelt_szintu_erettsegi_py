x = open(file='2014_majus\\verseny.txt',mode='r+').read().split('\n')
versenyzok_szama = x[0]
x.pop(0)
x.pop(-1)
#print(versenyzok_szama)
#print(x)

lst = []

#print(len(x))
for i in range(len(x)):
    lst2 = []
    for j in x[i]:
        if j == '+':
            lst2.append(1)
        else:
            lst2.append(0)
    lst.append(lst2)
print(lst)

print('2. feladat')
for i in range(len(lst)):
    talalat = 0
    for j in lst[i]:
        if j == 1:
            talalat += 1
        elif j == 0:
            talalat = 0
        if talalat == 2:
            print(i+1, end=' ')
            break

print('\n3. feladat')
lovesek_szama = []
for i in range(len(lst)):
    lovesek = len(lst[i])
    lovesek_szama.append(lovesek)

for i in range(len(lovesek_szama)):
    if lovesek_szama[i] == max(lovesek_szama):
        print(i+1)


def loertek(sor):
    aktpont = 20
    ertek = 0
    for i in range (len(sor)):
        if aktpont > 0 and sor[i] == '0':
            aktpont -= 1
        else: 
            ertek += aktpont
    return ertek


print('5. feladat')

sorszam = 1

talalt_lovesek = []

for i in range(len(lst[sorszam-1])):
    if lst[sorszam-1][i] == 1:
        talalt_lovesek.append(i+1)

print(talalt_lovesek)

talalt_lovesek_szama = 0

for i in lst[sorszam-1]:
    if i == 1:
        talalt_lovesek_szama += 1

print(talalt_lovesek_szama)

talalt_lovesek_sorozatai = []

sorozat = 0
for i in lst[sorszam-1]:
    if i == 1:
        sorozat += 1
        talalt_lovesek_sorozatai.append(sorozat)
    else:
        sorozat = 0
        talalt_lovesek_sorozatai.append(sorozat)
        

print(max(talalt_lovesek_sorozatai))

sztringxd = ''

for i in lst[sorszam-1]:
    if i == 1:
        sztringxd += '1'
    else:
        sztringxd += '0'

print(loertek(sztringxd))

print('6. feladat')

sorrend = []

for i in range(len(lst)):
    versenyzo = []

    versenyzo.append(0)

    versenyzo.append(i+1)

    sztringlol = ''
    for j in lst[i]:
        if j == 1:
            sztringlol += '1'
        else:
            sztringlol += '0'

    versenyzo.append(loertek(sztringlol))
    sorrend.append(versenyzo)

print('xd',sorrend)

pontszamok = []

for i in range(len(sorrend)):
    pontszamok.append(sorrend[i][2])
pontszamok.sort(reverse=True)
print(pontszamok)

sorrend2 = []

for i in range(len(sorrend)):
    for j in range(len(sorrend)):
        if pontszamok[i] == sorrend[j][2]:
            sorrend2.append(sorrend[j])

print('\n','asdadasd',sorrend2)

for i in range(len(sorrend2)):
    if sorrend2[i][0] == 0:
        if i == len(sorrend2)-1:
            sorrend2[i][0] = i+1
        elif sorrend2[i][2] != sorrend2[i+1][2]:
            sorrend2[i][0] = i+1
        else:
            sorrend2[i][0] = i+1
            sorrend2[i+1][0] = i+1
print('\n',sorrend2)