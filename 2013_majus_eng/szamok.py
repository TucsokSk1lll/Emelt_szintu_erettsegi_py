x = open(file='2013_majus_eng\\felszam.txt',mode='r').read().split('\n')
lst = []
lst2 = []
lst3 = []
#print(x)

for i in range(0,len(x),2):
    lst.append(x[i-1].split(' '))

#print(lst)

for i in range(0,len(x),2):
    lst3.append(x[i])
    for j in range(3):
        lst3.append(lst[int(i/2)][j])
    lst2.append(lst3)
    lst3 = []

print(lst2)

print('2.feladat')
print(len(lst2))

print('3.feladat')
cuccos = [0,0,0,0]
for i in range(len(lst2)):
    if lst2[i][3] == 'matematika':
        cuccos[0] += 1
        if lst2[i][2] == '1':
            cuccos[1] += 1
        if lst2[i][2] == '2':
            cuccos[2] += 1
        if lst2[i][2] == '3':
            cuccos[3] += 1

print(cuccos)

print('4.feladat')
terjedelem = [99999,0]

for i in range(len(lst2)):
    if int(lst2[i][1]) < terjedelem[0]:
        terjedelem[0] = int(lst2[i][1])
    if int(lst2[i][1]) > terjedelem[1]:
        terjedelem[1] = int(lst2[i][1])

print(terjedelem[1] - terjedelem[0])
