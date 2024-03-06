x = open(file='2014_oktober\\foglaltsag.txt',mode='r')
x = x.read()
lst = x.split('\n')
lst.pop()
print(lst)

y = open(file='2014_oktober\kategoria.txt',mode='r')
y = y.read()
lst2 = y.split('\n')
print(lst2)

print('2.feladat')
sor = 1
oszlop = 1

if lst[sor-1][oszlop-1] == 'x':
    print('foglalt')
else:
    print('nem foglalt')

print('3.feladat')
összesen = 20*15
eladott = 0
összesen = 0
egy = 0
ketto = 0
harom = 0
negy = 0
ot = 0

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if(lst2[i][j]) == '1':
            egy += 1
        if(lst2[i][j]) == '2':
            ketto += 1
        if(lst2[i][j]) == '3':
            harom += 1
        if(lst2[i][j]) == '4':
            negy += 1   
        if(lst2[i][j]) == '5':
            ot += 1   
        if lst[i][j] == 'x':
            eladott += 1
            összesen += 1
            
        else:
            összesen += 1
print(eladott,összesen,'szazalek:',round(eladott/összesen*100))

print('4.feladat')

print(egy,ketto,harom,negy,ot)

if egy > ketto and egy > harom and egy > negy and egy > ot:
    print('egy')

if ketto > egy and ketto > harom and ketto > negy and egy > ot:
    print('ketto')

if harom > ketto and harom > egy and harom > egy and egy > ot:
    print('harom')

if negy > egy and negy > ketto and negy > harom and egy > ot:
    print('negy')

if ot > egy and ot > ketto and ot > harom and ot > negy: 
    print('ot')
print('5.feladat')

print(egy*5000+ketto*4000+harom*3000+1500*ot+negy*2000)

print('6.feladat')
egyedulallo1 = 0
egyedulallo2 = 0
egyedulallo3 = 0

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j == 0:
            if lst[i][j] == 'o' and lst[i][j+1] == 'x':
                egyedulallo1 += 1
        if j == len(lst[i])-1:
            if lst[i][j] == 'o' and lst[i][j-1] == 'x':
                egyedulallo2 += 1
        if j != 0 and j != len(lst[i])-1: 
            if lst[i][j] == 'o' and lst[i][j+1] == 'x' and lst[i][j-1] == 'x':
                egyedulallo3 += 1
                #print(lst[i][j-1],lst[i][j],lst[i][j+1],i,j)


print(egyedulallo1+egyedulallo2+egyedulallo3)