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

    