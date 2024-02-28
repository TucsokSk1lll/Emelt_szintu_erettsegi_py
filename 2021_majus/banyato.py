x = open(file='C:\\Users\\gyo.joz.2008.01.TAG\\Documents\\webpage\\Emelt_szintu_erettsegi_py\\Melyseg\\melyseg.txt',mode='r')
x = x.read()
x = x.split('\n')
lul = []
lul.append(x[0])
lul.append(x[1])
x.pop(0)
x.pop(0)
for i in range(len(x)):
    x[i] = x[i].split(' ')
x.pop()
print(x)
print(lul)

print('2. feladat')
sor = 12
oszlop = 6
print(x[sor-1][oszlop-1])

print('3. feladat')

terület = 0
mélységek = [ ]
mélységek_összeg = 0

for i in range(len(x)):
    for j in range(len(x[i])):
        if x[i][j] != '0':
            terület += 1
            mélységek.append(x[i][j])

for i in range(len(mélységek)):
    mélységek_összeg += int(mélységek[i])

print(terület)
print(str(mélységek_összeg / int(len(mélységek)) / 10)[0:4])

print('4.feladat')

legmelyebb = 0
legmelyebb_lst = [ ]

for i in range(len(x)):
    for j in range(len(x[i])):
        if int(x[i][j]) > int(legmelyebb):
            legmelyebb = x[i][j]
            legmelyebb_lst = []
            legmelyebb_lst.append([i+1,j+1])
        elif x[i][j] == legmelyebb:
            legmelyebb = x[i][j]
            legmelyebb_lst.append([i+1,j+1])

#print(legmelyebb)
print(legmelyebb_lst)

print('5.feladat')
kerulet = 0
y = 0

for i in range(len(x)):
    for j in range(len(x[i])):
        if i >= 1 and j >= 1:
            y = 4
            if int(x[i][j]) != 0:
                if int(x[i-1][j]) >= 1:
                    y-=1
                if int(x[i+1][j]) >= 1:
                    y-=1
                if int(x[i][j-1]) >= 1:
                    y-=1
                if int(x[i][j+1]) >= 1:
                    y-=1
                kerulet += y

print(kerulet)

print('6.feladat')
oszlop = 6

diagram = open("diagram.txt", "w+")

for i in range(len(x)):
    
    diagram.write('0'+str(i+1))
    for i in range(round(int(x[i][oszlop-1])/10)):
        diagram.write('*')
    diagram.write('\n')
