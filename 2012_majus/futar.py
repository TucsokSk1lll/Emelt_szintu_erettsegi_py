x = open(file='2012_majus\\tavok.txt',mode='r').read().split('\n')

#print(x)
lst = []

for i in range(len(x)):
    lst.append(x[i].split(' '))
lst.pop()
print(lst)
    
print('2. feladat')

for i in range(len(lst)):
    if lst[i][1] == '1':
        print(lst[i][2])
        break

print('3. feladat')

utolso_ut = 0

for i in range(len(lst)):
    if lst[i][0] == '7' and int(lst[i][1]) > int(utolso_ut):
        utolso_ut = lst[i][1]

#print(utolso_ut)

for i in range(len(lst)):
    if lst[i][1] == utolso_ut and lst[i][0] == '7':
        print(lst[i][2])
        break

print('4. feladat')

napok = []

for i in range(len(lst)):
    if lst[i][0] not in napok:
        napok.append(lst[i][0])

#print(napok)
    
for i in range(7):
    if str(i+1) not in napok:
        print(i+1)

print('5. feladat')

fuvarok = []

for i in range(7):
    lst2 = []
    lst2.append(str(i+1))
    lst2.append(0)
    fuvarok.append(lst2)

for i in range(len(lst)):
    for j in range(7):
        if lst[i][0] == fuvarok[j][0]:
            fuvarok[j][1] += int(1)  

#print(fuvarok) 

legtobb = [0,0]

for i in range(len(fuvarok)):
    if fuvarok[i][1] > legtobb[1]:
        legtobb = fuvarok[i]

print(legtobb[0])

print('6. feladat')

tekersek = []

for i in range(7):
    lst2 = []
    lst2.append(str(i+1))
    lst2.append(0)
    tekersek.append(lst2)

for i in range(len(lst)):
    for j in range(7):
        if lst[i][0] == tekersek[j][0]:
            tekersek[j][1] += int(lst[i][2])

#print(tekersek)

legtobb2 = [0,0]

for i in range(len(tekersek)):
    if tekersek[i][1] > legtobb2[1]:
        legtobb2 = tekersek[i]

print(legtobb2[0])

print('7. feladat')

tetszoleges_szam = 0

def berezes(tetszoleges_szam):
    if tetszoleges_szam <= 2 and tetszoleges_szam > 0:
        return('500ft')
        print('500ft')
    elif tetszoleges_szam <= 5 and tetszoleges_szam > 2:
        return('700ft')
        print('700ft')
    elif tetszoleges_szam <= 10 and tetszoleges_szam > 5:
        return('900ft')
        print('900ft')
    elif tetszoleges_szam <= 20 and tetszoleges_szam > 10:
        return('1400ft')
        print('1400ft')
    elif tetszoleges_szam <= 30 and tetszoleges_szam > 20:
        return('2000ft')
        print('2000ft')
    elif tetszoleges_szam == 0:
        return('0ft')
        print('SIKE that is the wrong number')

print(berezes(tetszoleges_szam))

#8.feladat

dijazas = open(file='2012_majus\\dijazas.txt',mode='w')

for i in range(len(lst)):
    pass