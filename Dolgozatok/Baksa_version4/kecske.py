lst = open('Dolgozatok\\kecske\\meccs.txt','r').read().split('\n')
merkozesek_szama = int(lst[0])
lst.pop(0)
lst.pop()
for i in range(len(lst)):
    lst[i] = lst[i].split(' ')

#print(lst)
#print(merkozesek_szama)

print('2.feladat')
szam = int(input('szam: '))
fordulo = []

for i in lst:
    if i[0] == str(szam):
        fordulo.append(i)

for i in range(len(fordulo)):
    print(f'{fordulo[i][5]}-{fordulo[i][6]}: {fordulo[i][1]}-{fordulo[i][2]} ({fordulo[i][3]}-{fordulo[i][4]})')

print('3.feladat')
forditasok = []
for i in range(len(lst)):
    if (int(lst[i][1]) < int(lst[i][2]) and int(lst[i][3]) > int(lst[i][4])) or (int(lst[i][1]) > int(lst[i][2]) and int(lst[i][3]) < int(lst[i][4])):
        forditasok.append(lst[i])
        
#print(forditasok)

for i in range(len(forditasok)):
    if int(forditasok[i][1]) > int(forditasok[i][2]):
        print(f'{forditasok[i][0]} {forditasok[i][5]}')
    else:
        print(f'{forditasok[i][0]} {forditasok[i][6]}')

print('4.feladat')
csapat = input('Csapat: ')

print('5.feladat')
golok = [0,0]

for i in range(len(lst)):
    if lst[i][5] == csapat:
        golok[0] += int(lst[i][1])
        golok[1] += int(lst[i][2])
    elif lst[i][6] == csapat:
        golok[0] += int(lst[i][2])
        golok[1] += int(lst[i][1])

print(f'lott: {golok[0]} kapott: {golok[1]}')

print('6.feladat')
adott = 'Bogarak'
kikapot = None
fordulo = None

for i in range(len(lst)):
    if lst[i][5] == adott and (int(lst[i][1]) < int(lst[i][2])):
        kikapot = lst[i][6]
        fordulo = lst[i][0]
        break
    elif lst[i][6] == adott and (int(lst[i][2]) < int(lst[i][1])):
        kikapot = lst[i][5]
        fordulo = lst[i][0]
        break

print(kikapot)
print(fordulo)

#print('7.feladat')
eredmenyek = []
for i in range(10):
    for j in range(10):
        eredmenyek.append([i,j,0])

#print(eredmenyek)

for i in range(len(lst)):
    if int(lst[i][1]) > int(lst[i][2]):
        for j in range(len(eredmenyek)):
            #print(eredmenyek[j][0] , int(lst[i][1]) , eredmenyek[j][1] , int(lst[i][2]))
            if eredmenyek[j][0] == int(lst[i][1]) and eredmenyek[j][1] == int(lst[i][2]):
                eredmenyek[j][2] += 1
                break
    elif int(lst[i][2]) > int(lst[i][1]):
        for j in range(len(eredmenyek)):
            if eredmenyek[j][0] == int(lst[i][2]) and eredmenyek[j][1] == int(lst[i][1]):
                eredmenyek[j][2] += 1
                break
    elif int(lst[i][2]) == int(lst[i][1]):
        for j in range(len(eredmenyek)):
            if eredmenyek[j][0] == int(lst[i][2]) and eredmenyek[j][1] == int(lst[i][1]):
                eredmenyek[j][2] += 1
                break

#print(eredmenyek)

stat = open('C:\\Users\\gyo.joz.2008.01\\Documents\\GitHub\\Emelt_szintu_erettsegi_py\\Dolgozatok\\kecske\\stat.txt', 'w')

for i in range(len(eredmenyek)):
    if eredmenyek[i][2] != 0:
        stat.write(f'{eredmenyek[i][0]}-{eredmenyek[i][1]}: {eredmenyek[i][2]} darab\n')