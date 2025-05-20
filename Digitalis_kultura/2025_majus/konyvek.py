lst = open('Digitalis_kultura\\2025_majus\kiadas2.txt','r',encoding='UTF-8').read().split('\n')
for i in range(len(lst)):
    lst[i] = lst[i].split(';')
lst.pop()
print(lst)

print('2.feladat')
Szerzo = 'Benedek Elek'
darab = 0

for i in lst:
    
    if Szerzo in i[3]:
        darab += 1
        
print(f'{darab} konyvkiadas')

print('3.feladat')
legnagyobb = 0
elofordult = None
for i in lst:
    if int(i[4]) > legnagyobb:
        legnagyobb = int(i[4])
        elofordult = 1
    elif int(i[4]) == legnagyobb:
        elofordult += 1
        
print(f'Legnagyobb példányszám: {legnagyobb}, előfordult {elofordult} alkalommal ')

print('4.feladat')
peldany = ['6666','4','kf','kecske','69']

for i in lst:
    if int(i[4]) >= 40000 and i[2] == 'kf'and (int(i[0]) < int(peldany[0]) or (int(i[0]) == int(peldany[0]) and int(i[1]) < int(peldany[1]))):
        peldany = i 
        
print(f'{peldany[0]}/{peldany[1]}. {peldany[3]}')

print('5.feladat')
dic = {
	2020:{'magyar_kiadas':0,'magyar_peldany':0,'kulfoldi_kiadas':0,'kulfoldi_peldany':0},
	2021:{'magyar_kiadas':0,'magyar_peldany':0,'kulfoldi_kiadas':0,'kulfoldi_peldany':0},
	2022:{'magyar_kiadas':0,'magyar_peldany':0,'kulfoldi_kiadas':0,'kulfoldi_peldany':0},
	2023:{'magyar_kiadas':0,'magyar_peldany':0,'kulfoldi_kiadas':0,'kulfoldi_peldany':0}
}

for i in lst:
    if i[2] == 'ma':
        dic[int(i[0])]['magyar_kiadas'] += 1
        dic[int(i[0])]['magyar_peldany'] += int(i[4])
    elif i[2] == 'kf':
        dic[int(i[0])]['kulfoldi_kiadas'] += 1
        dic[int(i[0])]['kulfoldi_peldany'] += int(i[4])
        
print(dic)

print('6.feladat')
tobbszor_kiadottak = []

for i in range(len(lst)):
	szam = 0
	peldanyszam = int(lst[i][4])

	for j in range(i+1,len(lst)):
		if lst[i][3] == lst[j][3] and int(lst[j][4]) > peldanyszam:
			szam += 1
			#print(lst[j],peldanyszam)
		if szam == 2 and lst[i][3] not in tobbszor_kiadottak:
			tobbszor_kiadottak.append(lst[i][3])
            
print(tobbszor_kiadottak)