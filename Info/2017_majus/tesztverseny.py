megoldas = 'BCCCDBBBBCDAAA'
x = open(file='2017_majus\\valaszok.txt',mode='r')
x = x.read()
x = x.split('\n')
x.pop()
print(x)

lst = []

for i in range(len(x)):
    for j in range(len(x[i])):
        lst2 = [ ]
        if(x[i][j] == ' '):
            lst2.append(x[i][0:j])
            lst2.append(x[i][j+1:len(x[i])])
            lst.append(lst2)
            break

print(lst)

print('2. feladat')
versenyzok_szama = len(lst)
print('A vetélkedőn ' + str(len(lst)) + ' versenyző indult.')

print('3. feladat')
azonosito = 'AB123'
valasz = None

for i in range(len(lst)):
    #print(lst[])
    if lst[i][0] == azonosito:
        print(str(lst[i][1]) + '    (a versenyzo valasza)')
        valasz = str(lst[i][1])
        break

print('4. feladat')
print(str(megoldas) + '    (helyes megoldas)')

for i in range(len(valasz)):
    if valasz[i] == megoldas[i]:
        print('+',end='')
    else:
        print(' ',end='')
print('\n')

print('5.feladat')
sorszam = 10
valaszok = 0

for i in range(len(lst)):
    if lst[i][1][sorszam-1] == megoldas[sorszam-1]:
        valaszok += 1

xd = valaszok/versenyzok_szama*100

print('A feladatra ' + str(valaszok) + ' fo, a versenyzok ' + str(xd)[0:5] + '%' + '-a adott helyes valaszt.')

print('6.feladat')



pontok = open("pontok.txt","w")

for i in range(len(lst)):
    hanyadik = 0
    pontszam = 0
    #print(lst[i][1])
    for j in range(len(lst[i][1])):
        hanyadik += 1
        #print(lst[i][1][j],megoldas[j])
        if lst[i][1][j] == megoldas[j]:
            #print('YEEEEY')
            if hanyadik <= 5:
                pontszam += 3
            elif hanyadik > 5 and hanyadik <=10:
                pontszam += 4
            elif hanyadik > 10 and hanyadik <= 13:
                pontszam += 5
            elif hanyadik == 14:
                pontszam += 6       
     #print(lst[i][0],pontszam)   
    pontok.write(str(lst[i][0]))
    pontok.write(' ')
    pontok.write(str(pontszam))
    pontok.write('\n')  

pontok.close()
print('7.feladat')

y = open(file='C:\\Users\\gyo.joz.2008.01.TAG\\Documents\\webpage\\pontok.txt',mode='r')
y = y.read()
y = y.split('\n')
#print(y)
#print('AAAAAAAA')

legjobbak = []

lstb = [ ]

for i in range(len(y)):
    lstb2 = [ ]
    #print(y[i].split(' '))
    lstb.append(y[i].split(' '))
lstb.pop()

#print(lstb)

dict = {}
for i in range(len(lstb)):
    dict.update({lstb[i][0]:int(lstb[i][1])})
print(max(dict.values()))