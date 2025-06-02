print('1.feladat')
konyv = open('Digitalis_kultura\\2025_majus_eng\konyv.txt','r').read().split('\n')

for i in konyv:
    print(i)

print('2.feladat')
szam = 3
leghosszabb = 0

for i in konyv:
    if len(i) > leghosszabb:
        leghosszabb = len(i)
  
for i in konyv:
	print(szam*str(str(i)+' '*(leghosszabb-len(i)+1)+'|'))
 
#print('3.feladat')
def atalakit(sor):
    atalakitott = ''
    
    for i in range(0,len(sor),2):
        atalakitott += int(sor[i])*str(sor[i+1])
        
    return atalakitott

print('4.feladat')
szg = open('Digitalis_kultura\\2025_majus_eng\\szg_t.txt','r').read().split('\n')
with open('szg.txt','w') as xd:
	for i in szg:
		print(atalakit(i))
		xd.write(f'{atalakit(i)}\n')
  
print('5.feladat')
tomoritett = 'konyv_t.txt'
tomoritetlen = 'konyv.txt'

tomoritett_str = open(f'Digitalis_kultura\\2025_majus_eng\\{tomoritett}').read()
tomoritettlen_str = open(f'Digitalis_kultura\\2025_majus_eng\\{tomoritetlen}').read()


tomoritett_szam = len(tomoritett_str)-len(tomoritett_str.split('\n'))+1
tomoritetlen_szam = len(tomoritettlen_str)-len(tomoritettlen_str.split('\n'))+1

print(f'A karakterek száma a tömörített állományban: {tomoritett_szam}')
print(f'A karakterek száma a tömörítetlen állományban: {tomoritetlen_szam}')
print(f'A tömörítési arány: {round(tomoritett_szam/tomoritetlen_szam,2)}')

print('6.feladat')
aszki = open('Digitalis_kultura\\2025_majus_eng\konyv_t.txt','r').read().split('\n')

print(f'Az ábra magassága sorokban: {len(aszki)}')


leghosszabb = 0
blokk = 0

for i in range(len(aszki)):
	hossz = 0
	for j in range(0,len(aszki[i]),2):
		hossz += int(aszki[i][j])
		blokk += 1
	if hossz > leghosszabb:
		leghosszabb = hossz
  
print(f'Az ábra szélessége karakterekben: {leghosszabb}')
print(f'A blokkok száma: {blokk}')
