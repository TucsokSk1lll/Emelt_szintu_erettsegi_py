x = open(file='C:\\Users\\jgyor\\OneDrive\\Dokumentumok\\GitHub\\Emelt_szintu_erettsegi_py\\Baksa_version3\\emberek.txt',mode='r').read().split('\n')

for i in range(len(x)):
    x[i] = x[i].split(' ')

lst = x

#print(lst)

print('2. feladat')
print('50-150 evesek:')

for i in range(len(lst)):
    if int(lst[i][0]) >= 50 and int(lst[i][0]) <= 150:
        print(lst[i][1] + ' ' + lst[i][2] + ' ' + lst[i][0])

print('3.feladat')

for i in range(len(lst)):
    if lst[i][1][0:1] == 'B' and lst[i][2][0:1] == 'B':
        print(lst[i][1] + ' ' + lst[i][2])

print('4.feladat')

eletkorok = []

for i in range(len(lst)):
    if int(lst[i][0]) >= 10 and int(lst[i][0]) <= 50:
        eletkorok.append(int(lst[i][0]))

atlag = None
osszeg = 0


for i in range(len(eletkorok)):
    osszeg += eletkorok[i]


print('A fiatalok atlageletkora: ' + str(osszeg/len(eletkorok))[0:5])

#5.feladat

ki = open(file='C:\\Users\\jgyor\\OneDrive\\Dokumentumok\\GitHub\\Emelt_szintu_erettsegi_py\\Baksa_version3\\ki.txt', mode='w')

for i in range(len(lst)):
    if int(lst[i][0]) >= 150 and int(lst[i][0]) <= 200 and len(lst[i][1]) == 5:
        ki.write(lst[i][0] + ' ' + lst[i][1] + ' ' + lst[i][2] + '\n')
        #print(lst[i][0] + ' ' + lst[i][1] + ' ' + lst[i][2])


