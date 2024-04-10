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
szazalekok = {}

for i in range(len(x)):
    szazalekok[str(x[i][2]) + ' ' + str(x[i][3])] = x[i][1]

for i in szazalekok.keys():
    print(i)


