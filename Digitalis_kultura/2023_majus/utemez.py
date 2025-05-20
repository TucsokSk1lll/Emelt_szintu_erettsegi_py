<<<<<<< HEAD
lst = open('Digitalis_kultura\\2023_majus\\taborok.txt','r').read().split('\n')
for i in range(len(lst)):
	lst[i] = lst[i].split('\t')
lst.pop()
for i in range(len(lst)):
    for j in range(len(lst[i])):
        try:
            lst[i][j] = int(lst[i][j])
        except:
            pass
print(lst)

print('2.feladat')
print(f'Az először rögzített tábor témája: {lst[0][5]}\nAz utoljára rögzített tábor témája: {lst[-1][5]}')

print('3. feladat')
vane = False
for i in range(len(lst)):
	if lst[i][5] == 'zenei':
		print(f'Zenei tábor kezdődik {lst[i][0]}. hó {lst[i][1]}. napján.')
		vane = True
if vane == False:
    print('Nem volt zenei tábor.')
    
print('4.feladat')
y = []

for i in lst:
    y.append(len(i[4]))

k = None
for i in range(len(y)):
    if y[i] == max(y):
        k = i
        
print(f'Legnépszerűbbek:\n{lst[k][0]} {lst[k][1]} {lst[k][5]}')

#print('5.feladat')
=======
x = open('Digitalis_kultura\\2023_majus\\taborok.txt','r').read().split('\n')
x.pop()
#print(x)

lst = []

for i in range(len(x)):
    lst.append(x[i].split('\t'))
print(lst)

print('2.feladat')
print(f'Az adatsorok szama: {len(lst)}')

print('3.feladat')

taborok = []

for i in range(len(lst)):
    if lst[i][5] == 'zenei':
        taborok.append(lst[i])

if len(taborok) > 0:
    for i in taborok:
        print(f'Zenei tabor kezdodik {i[0]}. ho {i[1]}. napjan. ')
else:
    print('Nem volt zenei tábor.')

print('4.feladat')
legnepszerubbek = []

legtobb = 0

for i in range(len(lst)):
    if len(lst[i][4]) > legtobb:
        legtobb = len(lst[i][4])

for i in range(len(lst)):
    if len(lst[i][4]) == legtobb:
        legnepszerubbek.append(lst[i])

for i in range(len(legnepszerubbek)):
    print(f'{legnepszerubbek[i][0]} {legnepszerubbek[i][1]} {legnepszerubbek[i][5]}')

#print('5.feladat')

>>>>>>> 67984d822a462c7d2cba364b18935bf7aea8eb43
def sorszam(honap,nap):
    napok = 0
    if honap == 6:
        napok += 0
        napok += nap-15
    if honap == 7:
        napok += 30-15
        napok += nap
    if honap == 8:
        napok += 30-15+31
        napok += nap
    return napok

print('6.feladat')
<<<<<<< HEAD
hó = 8
nap = 1

taborok = 0
for i in range(len(lst)):
    if sorszam(lst[i][0],lst[i][1]) <= sorszam(hó,nap) and sorszam(lst[i][2],lst[i][3]) >= sorszam(hó,nap):
        taborok += 1
        
print(f'Ekkor éppen {taborok} tábor tart.')

print('7.feladat')
erdeklodott = []


for i in range(len(lst)):
    if 'L' in lst[i][4]:
        erdeklodott.append([sorszam(lst[i][0],lst[i][1]),lst[i]])
        
#print(erdeklodott)

erdeklodott_sorted = []
while len(erdeklodott_sorted) != len(erdeklodott):
	legkisebb = [78,[69,69]]
	for i in range(len(erdeklodott)):
		if erdeklodott[i][0] < legkisebb[0] and erdeklodott[i] not in erdeklodott_sorted:
			legkisebb = erdeklodott[i]
			#print(erdeklodott[i])
	erdeklodott_sorted.append(legkisebb)
 
print(erdeklodott_sorted)

    
=======
ho = 8
nap = 1

tart = 0

for i in range(len(lst)):
    #print(sorszam(lst[i][0],lst[i][1]) , sorszam(ho,nap) , sorszam(lst[i][2],lst[i][3]) , sorszam(ho,nap))
    if sorszam(int(lst[i][0]),int(lst[i][1])) < sorszam(ho,nap) and sorszam(int(lst[i][2]),int(lst[i][3])) > sorszam(ho,nap):
        tart += 1

print(f'Ekkor eppen {tart} tabor tart.')

print('7.feladat')
betu = 'L'

erdeklodott = []

for i in range(len(lst)):
    if betu in lst[i][4]:
        erdeklodott.append(lst[i])

erdeklodott_sorted = []
datumok = []

for i in range(len(erdeklodott)):
    #print(int(erdeklodott[i][0]),int(erdeklodott[i][1]))
    datumok.append(sorszam(int(erdeklodott[i][0]),int(erdeklodott[i][1])))
datumok.sort()

#print(datumok)
#print(erdeklodott)

for j in range(len(datumok)):
    for i in range(len(erdeklodott)):
        if sorszam(int(erdeklodott[i][0]),int(erdeklodott[i][1])) == datumok[j] and erdeklodott[i] not in erdeklodott_sorted:
            erdeklodott_sorted.append(erdeklodott[i])

print(erdeklodott_sorted)

elmehet = True

for i in range(len(erdeklodott_sorted)):
    for j in range(len(erdeklodott_sorted)):
        datum1_kezdes = sorszam(int(erdeklodott[i][0]),int(erdeklodott[i][1])) 
        datum1_vege = sorszam(int(erdeklodott[i][2]),int(erdeklodott[i][3]))
        datum2_kezdes = sorszam(int(erdeklodott[j][0]),int(erdeklodott[j][1]))
        datum2_vege = sorszam(int(erdeklodott[j][2]),int(erdeklodott[j][3]))
        
        if (datum1_kezdes < datum2_kezdes and datum1_vege < datum2_kezdes) == False and (datum1_kezdes > datum2_vege and datum1_vege > datum2_vege) == False:
            elmehet = False
            break

if elmehet == True:
    print('Elmehet mindegyik taborba.')
else:
    print('Nem mehet el mindegyik taborba.')
>>>>>>> 67984d822a462c7d2cba364b18935bf7aea8eb43
