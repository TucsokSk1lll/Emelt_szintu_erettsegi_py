lst = open('Informatika\\2022_majus\\utca.txt','r').read().split('\n')
savok = lst[0].split(' ')
lst.pop()
lst.pop(0)
for i in range(len(savok)):
    savok[i] = int(savok[i])
print(savok)
for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
print(lst)

print('2.feladat')
print(f'A mintaban {len(lst)} telek szerepel.')

print('3.feladat')
adoszam = '68396'

for i in lst:
    if i[0] == adoszam:
        print(f'{i[1]} utca {i[2]}')

print('4.feladat')
def ado(sav,terulet):
    monej = 0
    if sav == 'A':
        monej += terulet*savok[0]
    if sav == 'B':
        monej += terulet*savok[1]
    if sav == 'C':
        monej += terulet*savok[2]
    return monej

print('5.feladat')
epuletek = [[0,0],[0,0],[0,0]]

for i in lst:
    if i[3] == 'A':
        epuletek[0][0] += 1
        epuletek[0][1] += int(i[4])*savok[0]
    if i[3] == 'B':
        epuletek[1][0] += 1
        epuletek[1][1] += int(i[4])*savok[1]
    if i[3] == 'C':
        epuletek[2][0] += 1
        epuletek[2][1] += int(i[4])*savok[2]

print(f'A savba {epuletek[0][0]} telek esik, az ado {epuletek[0][1]} Ft.')
print(f'B savba {epuletek[1][0]} telek esik, az ado {epuletek[1][1]} Ft.')
print(f'C savba {epuletek[2][0]} telek esik, az ado {epuletek[2][1]} Ft.')

print('6.feladat')
utcak = []
for i in lst:
    for j in lst:
        #print(i[1] , j[1] , i[2] , j[2] , i[3] , j[3] , i[1] not in utcak)
        #print(i[1] == j[1] , i[2] == j[2] , i[3] != j[3] , i[1] not in utcak)
        if i[1] == j[1] and i[3] != j[3] and i[1] not in utcak:
            utcak.append(i[1])

print(utcak)

print('7.feladat')
tulajok = []

for i in lst:
    if [i[0],0] not in tulajok:
        tulajok.append([i[0],0])

for i in lst:
    for j in range(len(tulajok)):
        if i[0] == tulajok[j][0]:
            if i[3] == 'A':
                tulajok[j][1] += int(i[4])*savok[0]
            if i[3] == 'B':
                tulajok[j][1] += int(i[4])*savok[1]
            if i[3] == 'C':
                tulajok[j][1] += int(i[4])*savok[2]

for i in range(len(tulajok)):
    if tulajok[i][1] < 10000:
        tulajok[i][1] = 0

print(tulajok)

fizetendo = open('Informatika\\2022_majus\\fizetendo.txt','w')
for i in tulajok:
    fizetendo.write(f'{i[0]} {i[1]}\n')