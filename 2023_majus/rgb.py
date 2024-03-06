x = open(file="2023_majus\\kep.txt", mode="r+")
x = x.read()
#print(x)
lst = []
cut = 0
cut2 = 0
spaces = 0
lst2 = []
for i in range(len(x)): 
    if x[i] == " " or x[i] == "\n":
        lst2.append(x[cut2:i])
        cut2 = i+1
        spaces += 1
    if spaces == 3:
        spaces = 0
        cut = i+1
        lst.append(lst2)
        lst2 = []
#print(lst)

sor = 1
oszlop = 1

print('2. feladat')
print(lst[(sor-1)*640+(oszlop-1)])

print('3. feladat')
vilagos = 0

for i in lst:
    if int(i[0])+int(i[1])+int(i[2]) > 600:
        vilagos += 1
        
print(vilagos)

print('4. feladat')
legsotetebb = 999999999
legsotetebb_lst = []

for i in lst:
    if int(i[0])+int(i[1])+int(i[2]) < legsotetebb:
        legsotetebb_lst = []
        legsotetebb_lst.append(i)
        legsotetebb = int(i[0])+int(i[1])+int(i[2])
    elif int(i[0])+int(i[1])+int(i[2]) == legsotetebb:
        legsotetebb_lst.append(i)
        
print(legsotetebb_lst)
print(legsotetebb)

def felho(sor, elteres):
    for i in range(639):
        #print(int(lst[(sor-1)*640+i][2])-elteres, int(lst[(sor-1)*640+i+1][2]))
        if int(lst[(sor-1)*640+i][2])-elteres > int(lst[(sor-1)*640+i+1][2]) or int(lst[(sor-1)*640+i][2])+elteres < int(lst[(sor-1)*640+i+1][2]):
            
            return True
    return False  

print(felho(1, 10))
print('6. feladat')

for i in range(1,360):
    if felho(i, 10) == True:
        print(i)
        break

for i in range(360, 1, -1):
    if felho(i, 10) == True:
        print(i)
        break