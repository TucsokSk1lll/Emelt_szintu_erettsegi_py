lst = open('C:\\Users\\jgyor\\OneDrive\\Dokumentumok\\GitHub\\Emelt_szintu_erettsegi_py\\2024_oktober\\jeladas.txt','r').read().split('\n')
for i in range(len(lst)):
    lst[i] = lst[i].split('\t')
print(lst)

print('2.feladat')

print(f'Az utolsó jeladás időpontja {lst[-1][1]}:{lst[-1][2]}, a jármű rendszáma {lst[-1][0]}')

print('3.felada')

elso = lst[0][0]

print(f'Az első jármű: {elso}')

jeladasok = []

for i in lst:
    if i[0] == elso:
        jeladasok.append(f'{i[1]}:{i[2]}')
        
print(f'jeladasainak idopontjai: {jeladasok}')

print('4.feladat')

ora = '6'
perc = '54'

jeladasok_szama = 0

for i in lst:
    if i[1] == ora and i[2] == perc:
        jeladasok_szama += 1

print(f'Jeladasok szama: {jeladasok_szama}')

print('5.feladat')

legnagyobb_sebesseg = 0
autok = []

for i in lst:
    if int(i[3]) > legnagyobb_sebesseg:
        legnagyobb_sebesseg = int(i[3])
        
for i in lst:
    if int(i[3]) == legnagyobb_sebesseg:
        autok.append(i[0])
        
print(f'A legnagyobb sebesseg km/h: {legnagyobb_sebesseg}')
print(f'A jarmuvek: {autok}')

print('5.feladat')

rendszam = 'ZVJ-638'
check = []
belepes = None
kilometer = 0
sebesseg = 0

for i in lst:
	if i[0] == rendszam:
		if belepes == None:
			check.append([f'{i[1]}:{i[2]}',0.00])
			belepes = [i[1],i[2]]
			sebesseg = int(i[3])
		else:
			kilometer += (int(i[1]) - int(belepes[0])) * sebesseg
			kilometer += ((int(i[2]) - int(belepes[1]))/60) * sebesseg
			check.append([f'{i[1]}:{i[2]}',round(kilometer,1)])
			sebesseg = int(i[3])
			belepes = [i[1],i[2]]
   
print(check)
         
print('7.feladat')


actions = []
for i in lst:
    not_in = True
    
    for j in actions:
        if j[0] == i[0]:
            not_in = False
    
    if not_in == True:
        actions.append([i[0],23,59,0,0])

for i in range(len(actions)):
    for j in lst:
        if j[0] == actions[i][0]:
            if int(j[1]) < int(actions[i][1]):
                actions[i][1] = j[1]
                actions[i][2] = j[2]
            elif int(j[1]) == actions[1] and int(j[2]) < actions[2]:
                actions[i][1] = j[1]
                actions[i][2] = j[2]
            
            if int(j[3]) > int(actions[i][3]):
                actions[i][3] = j[1]
                actions[i][4] = j[2]
            elif int(j[1]) == actions[1] and int(j[2]) < actions[2]:
                actions[i][3] = j[1]
                actions[i][4] = j[2]
print(actions)