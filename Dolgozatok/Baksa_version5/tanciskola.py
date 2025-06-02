lst2 = open('Dolgozatok\\Baksa_version5\\tancrend.txt','r').read().split('\n')
lst2.pop()
print(lst2,'\n')

lst = []

lst3 = []
for i in lst2:
    if len(lst3) == 0 and i != i.capitalize():
        lst3.append(i)
    elif i == i.capitalize():
        lst3.append(i)
    elif len(lst3) != 0 and i != i.capitalize():
        lst.append(lst3)
        lst3 = []
        lst3.append(i)
print(lst)

print('2.feladat')
print(f'elso: {lst[0][0]} utolso:{ lst[-1][0]}')

print('3.feladat')
parok = 0

for i in lst:
    if i[0] == 'samba':
        parok += 1

print(f'A sambat {parok} par mutatta be.')

print('4. feladat')
tancok = []

for i in lst:
    if 'Vilma' in i and i[0] not in tancok:
        tancok.append(i[0])

print('Vilma ',end='')

for i in tancok:
    print(i,end=' ')

print('tancokban szerepelt.')

print('5.feladat')
kivel = None
tanc = input('tanc: ') #'rumba'

for i in lst:
    if 'Vilma' in i and i[0] == tanc:
        for j in i:
            if j != 'Vilma' and j == j.capitalize():
                kivel = j

if kivel != None:
    print(f'A {tanc} bemutatojan Vilma parja {kivel} volt.')
else:
    print(f'Vilma nem talcolt {tanc}t')

#print('6.feladat')
fiuk = []
lanyok = []

for i in lst:
    if i[1] not in lanyok:
        lanyok.append(i[1])
    if i[2] not in fiuk:
        fiuk.append(i[2])

szereplok = open('Dolgozatok\\Baksa_version5\\szereplok.txt','w')

szereplok.write('Lanyok: ')
for i in lanyok:
    szereplok.write(f'{i}, ')
szereplok.write('\n')

szereplok.write('Fiuk: ')
for i in fiuk:
    szereplok.write(f'{i}, ')

