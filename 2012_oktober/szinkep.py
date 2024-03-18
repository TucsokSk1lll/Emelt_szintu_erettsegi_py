x = open(file="2012_oktober\kep.txt", mode="r")
x = x.read()
x = x.split("\n")
x.pop()
for i in range(len(x)):
    x[i] = x[i].split(" ")

lst = []
lst2 = []
for i in range(50):
    index = 0
    for j in range(50):
        lst2.append(x[index])
        index += 1
    lst.append(lst2)

for i in range(50):
    for j in range(50):
        for k in range(3):
            lst[i][j][k] = int(lst[i][j][k])

print('2. feladat')
rgb = [200,96,69]
lol = False

for i in range(50):
    for j in range(50):
        if lst[i][j] == rgb:
            lol = True

print('3. feladat')

sor = 0
oszlop = 0

for i in range(50):
    for j in range(50):
        if i == 34 and lst[34][7] == lst[i][j]:
            sor += 1

for i in range(50):
    for j in range(50):
        if j == 7 and lst[34][7] == lst[i][j]:
            oszlop += 1

print(sor, oszlop, lst[34][7])
            