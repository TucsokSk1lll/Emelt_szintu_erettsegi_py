# File beolvasasa. Minden sor egy listaelem, és minden listaelemben minden szo egy listaelem.

x = open(file='2013_majus\\szavazatok.txt',mode='r+').read().split('\n')
for i in range(len(x)):
    x[i] = x[i].split(' ')

# Kiirja, hogy hanyan indultak a valasztason
# (a lista elemeinek a szamat)
print('2. feladat')
print(len(x))

# Bekeri egy indulo nevet. Ha az elso neve egyezik az egyik listaelem 3. elemevel, es a masodik neve egyezik a listaelem 4. elemevel, akkor irja ki hogy hany szavazatot kapott az illeto (a listaelem 2. elemet), kulonben irja ki hogy nincs ilyen indulo.
print('3. feladat')
indulo = 'Joghurt Jakab'
indulo = indulo.split(' ')
van_e_indulo = False
for i in range(len(x)):
    if x[i][2] == indulo[0] and x[i][3] == indulo[1]:
        print(x[i][1])
        van_e_indulo = True
        break
if not van_e_indulo:
    print('Ilyen nevu kepviselojelolt nem szerepel a nyilvantartasban!')

# Kiirja a reszveteli aranyt a valasztason. (ez csak egy szazalek szamitas lol, meg ossze kell szamolni a szavazatokat az remelem meg megy)
print('4. feladat')
szavazok = 0

for i in range(len(x)):
    szavazok += int(x[i][1])

szazalek = szavazok / 12345 * 100

if str(szazalek)[2] == '.':
    print(str(szazalek)[0:5] + '%')
else:
    print(str(szazalek)[0:4] + '%')

# Kiirja hogy a partok az osszes szavazat hany szazalekat kaptak.
# de hat ez ugyan az mint az elozo xd
print('5. feladat')
partok = [['-', 0]]
szavazatok = 0
for i in range(len(x)):
    szavazatok += int(x[i][1])

#print(x)

for i in range(len(x)):
    bennevane = False
    for j in range(len(partok)):
        #print(x[i][4], partok[j][0])
        if x[i][4] == partok[j][0]:
            #print(x[i][4], partok[j][0],'lol')
            bennevane = True
            break
    if not bennevane:
        partok.append([x[i][4], 0])

for i in range(len(x)):
    for j in range(len(partok)):
        if x[i][4] == partok[j][0]:
            partok[j][1] += int(x[i][1])

for i in range(len(partok)):
    partok[i].append(str(partok[i][1] / szavazatok * 100)[0:4] + '%')

for i in range(len(partok)):
    partok[i].pop(1)

partok[0][0] = 'Fuggetlenek'

print(partok)

print('6. feladat')
legtobb = ['fakexd',0]
for i in range(len(x)):
    jelolt = []
    if int(x[i][1]) > int(legtobb[1]):
        jelolt.append(str(x[i][2]+' '+x[i][3]))
        jelolt.append(x[i][1])
        legtobb = jelolt
        #print(legtobb)
    elif int(x[i][1]) == int(legtobb[1]):
        jelolt.append(str(x[i][2]+' '+x[i][3]))
        jelolt.append(x[i][1])
        legtobb.append(jelolt)
        #print(legtobb)
print(legtobb)

print('7.feladat')

keruletek = [[1,0,'fake','part'],[2,0,'fake','part'],[3,0,'fake','part'],[4,0,'fake','part'],[5,0,'fake','part'],[6,0,'fake','part'],[7,0,'fake','part'],[8,0,'fake','part']]

for i in range(len(x)):
    for j in range(len(keruletek)):
        if int(x[i][0]) == int(keruletek[j][0]):
            if int(x[i][1]) > int(keruletek[j][1]):
                keruletek[j] = x[i]

print(keruletek)