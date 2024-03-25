x = open(file='2014_majus\\verseny.txt',mode='r+').read().split('\n')
versenyzok_szama = x[0]
x.pop(0)
x.pop(-1)
#print(versenyzok_szama)
#print(x)

lst = []

#print(len(x))
for i in range(len(x)):
    lst2 = []
    for j in x[i]:
        if j == '+':
            lst2.append(1)
        else:
            lst2.append(0)
    lst.append(lst2)
print(lst)

print('2. feladat')
for i in range(len(lst)):
    talalat = 0
    for j in lst[i]:
        if j == 1:
            talalat += 1
        elif j == 0:
            talalat = 0
        if talalat == 2:
            print(i+1, end=' ')
            break

print('\n3. feladat')
lovesek_szama = []
for i in range(len(lst)):
    lovesek = len(lst[i])
    lovesek_szama.append(lovesek)

for i in lovesek_szama:
    if i == max(lovesek_szama):
        print(i+1)


print(lovesek_szama)
