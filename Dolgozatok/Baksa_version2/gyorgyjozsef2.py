x = open(file='Baksa_version2\\eloadas.txt',mode='r+').read().split('\n')
x.pop()
#print(x)

lst = []

for i in range(len(x)):
    lst.append(x[i].split(' '))

for i in range(len(lst)):
    if lst[i][0] == 'ď»ż1':
        lst[i][0] = '1'

#print(lst)

print('2.feladat')
print('A nyilvantartasban ' + str(len(lst)) + ' eloadas szerepel.')

print('3.feladat')
nap = input('Kerem a nap sorszamat: ')

for i in range(len(lst)):
    if lst[i][0] == str(nap):
        print(lst[i][1]+' '+lst[i][2]+' '+lst[i][3]+' '+lst[i][4])

print('4.feladat')
utolso_nap = 0

for i in range(len(lst)):
    if int(lst[i][0]) > utolso_nap:
        utolso_nap = int(lst[i][0])

print('A konferencia utolso napja: ' + str(utolso_nap))

#5.feladat

lista = open(file='Baksa_version2\\lista.txt',mode='w')

for i in range(len(lst)):
    if lst[i][4][0] == 'P':
        lista.write(str(lst[i][3]) + ' ' + str(lst[i][4]) + '\n')