import random
x = open(file='2013_majus_eng\\felszam.txt',mode='r').read().split('\n')
lst = []
lst2 = []
lst3 = []
#print(x)

for i in range(0,len(x),2):
    lst.append(x[i-1].split(' '))

#print(lst)

for i in range(0,len(x),2):
    lst3.append(x[i])
    for j in range(3):
        lst3.append(lst[int(i/2)][j])
    lst2.append(lst3)
    lst3 = []

print(lst2)

print('2.feladat')
print(len(lst2))

print('3.feladat')
cuccos = [0,0,0,0]
for i in range(len(lst2)):
    if lst2[i][3] == 'matematika':
        cuccos[0] += 1
        if lst2[i][2] == '1':
            cuccos[1] += 1
        if lst2[i][2] == '2':
            cuccos[2] += 1
        if lst2[i][2] == '3':
            cuccos[3] += 1

print(cuccos)

print('4.feladat')
terjedelem = [99999,0]

for i in range(len(lst2)):
    if int(lst2[i][1]) < terjedelem[0]:
        terjedelem[0] = int(lst2[i][1])
    if int(lst2[i][1]) > terjedelem[1]:
        terjedelem[1] = int(lst2[i][1])

print(terjedelem[1] - terjedelem[0])

print('5.feladat')

temakorok = []

for i in range(len(lst2)):
    if lst2[i][3] not in temakorok:
        temakorok.append(lst2[i][3])

print(temakorok)

print('6.feladat')

temakor = 'tortenelem'
kerdesek_szama = 0
random_szam = None
valasz = None
pont = 0

for i in range(len(lst2)):
    if lst2[i][3] == temakor:
        kerdesek_szama += 1

print(kerdesek_szama)
random_szam = random.randrange(0,kerdesek_szama)

for i in range(len(lst2)):
    if lst2[i][3] == temakor:
        random_szam -= 1
    if random_szam == 0:
        valasz = lst2[i][1]
        pont = lst2[i][2]
        print(lst2[i][0])

input_valasz = valasz
print(input_valasz)
print('A valasz ' + str(pont) + ' pontot er.')

if input_valasz != valasz:
    print('A helyes valsz: ' + str(valasz))

print('7.feladat')

random_szamok = []
maxxd = 0

for i in range(len(lst2)):
    for j in range(len(temakorok)):
        if lst2[i][3] == temakorok[j]:
            maxxd += 1

#print(maxxd)

while len(random_szamok) < 10:
    veletlen = random.randrange(0,maxxd)
    if veletlen not in random_szamok:
        random_szamok.append(veletlen)

#print(len(random_szamok))

tesztfel = open(file='2013_majus_eng\\tesztfel.txt',mode='w')

adhato_pontok = 0

for i in range(len(random_szamok)):
    adhato_pontok += int(lst2[random_szamok[i]][2])
    tesztfel.write(lst2[random_szamok[i]][2] + ' ' + lst2[random_szamok[i]][1] + ' ' + lst2[random_szamok[i]][0] + '\n')
tesztfel.write('A feladatsorra osszesen ' + str(adhato_pontok) + ' pont adhato.')