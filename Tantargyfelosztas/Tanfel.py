x = open(file='C:\\Users\\gyo.joz.2008.01.TAG\\Documents\\webpage\\Emelt_szintu_erettsegi_py\\Tantargyfelosztas\\beosztas.txt',mode='r')
x = x.read()
x = x.split('\n')
x.pop()
#print(x)
#print('\n')

lst = []
bejegyzesek = 0
tanitasi_orak = 0
random_tanar_orainak_szama = 0
tanarok_orak = []
csoportbontás = None
tanarok = []

for i in range(int(len(x)/4)):
    lst2 = []
    for j in range(4):
        lst2.append(x[j])
    bejegyzesek += 1
    for j in range(4):
        x.pop(0)
    lst.append(lst2)

#print(lst)
print('2. feladat')
print('A fajlban',bejegyzesek,'bejegyzes van.')

for i in range(len(lst)):
    tanitasi_orak += int(lst[i][3])

print('3.feladat')
print('Az iskolaban a heti osszoraszam:',tanitasi_orak)


random_tanar = input('Egy tanar neve= ')

for i in range(len(lst)):
    if lst[i][0] == random_tanar:
        random_tanar_orainak_szama += int(lst[i][3])

print('4. feladat')
print('Atanar heti oraszama:',random_tanar_orainak_szama)

file = open('of.txt','w')
lst4 = []

for i in range(len(lst)):
    lst3 = []
    lst3.append(lst[i][2])
    lst3.append(lst[i][0])
    if lst3 in lst4:
        pass
    else:
        lst4.append(lst3)
#print(lst4)

for i in range(len(lst4)):
    file.write(lst4[i][0])
    file.write(' - ')
    file.write(lst4[i][1])
    file.write('\n')

random_osztaly_tantargy = [['','']]

random_osztaly_tantargy[0][0] = input('Osztaly= ')
random_osztaly_tantargy[0][1] = input('Tantargy= ')

for i in range(len(lst)):
    if lst[i][2] == random_osztaly_tantargy[0] and lst[i][1] == random_osztaly_tantargy[1]:
        if(csoportbontás == None):
            csoportbontás = False
        elif csoportbontás == False:
            csoportbontás = True

print('6. feladat')
if csoportbontás == False:
    print('Nem csoportbontasban tanuljak.')
else:
    print('Csoportbontasban tanuljak.')


for i in range(len(lst)):
    if lst[i][0] in tanarok:
        pass
    else:
        tanarok.append(lst[i][0])

print('7. feladat')
print('Az iskolaban',len(tanarok),'tanar tanit.')