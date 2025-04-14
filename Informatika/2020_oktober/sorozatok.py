x = open(file='2020_oktober\\lista.txt',mode='r')
x = x.read()
x = x.split('\n')
#print(x)

lst = []

for i in range(int(len(x)/5)):
    lst2 = []
    for j in range(5):
        lst2.append(x[i*5+j])
    lst.append(lst2)

print(lst)

print("2.feladat")
asd = 0
for i in range(len(lst)):
    if lst[i][0] != 'NI':
        asd += 1
print(asd)

print('3.feladat')
xd = 0
for i in range(len(lst)):
    if lst[i][4] != '0':
        xd += 1
print(str(xd/len(lst)*100)[0:5])

print('4.feladat')
ido = 0
for i in range(len(lst)):
    for j in range(int(lst[i][4])):
        ido += int(lst[i][3])

nap = ido//60//24
ora = ((ido-(nap*24*60))//60)
perc = ((ido-(nap*24*60))%60)

print(nap,'napot',ora,'orat',perc,'percet')

print('5.feladat')
datum = '2017.10.18'
datumxd = 0

for i in lst:
    #print(i[0][0:4])
    if i[0][0:4] != 'NI':
        if int(i[0][0:4]) <= int(datum[0:4]):
            if int(i[0][5:7]) <= int(datum[5:7]):
                if int(i[0][8:10]) < int(datum[8:10]):
                    if int(i[4]) == 0:
                        print(i)

print('6.feladat')