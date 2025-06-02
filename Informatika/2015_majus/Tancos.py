lst = []
Samba = 0
Vilma_tancai = []
random_tanc = 'cha-cha'
fiuk = []
lanyok = []
szamlalo_fiu = {

}
szamlalo_lany = {

}
legtobbszor_fiu = []
legtobbszor_lany = []


x = open(file="Informatika\\2015_majus\\tancrend.txt", mode="r", encoding="utf-8")
x = x.read()
x =  x.split('\n')
x.pop()
for i in range(int(len(x)/3)-1):
    lst2 = []
    for j in range(3):
        lst2.append(x[j])
        if x[j] == 'samba':
            Samba += 1
        if x[j] == 'Vilma':
            Vilma_tancai.append(lst2[0])
        x.pop(0)
    lst.append(lst2)
print(lst)

print('Elso es utolso tanc: ',lst[0][0], lst[len(lst)-1][0])

print('Samba: ', Samba)

print('Vilma tancai: ', Vilma_tancai)

for i in range(len(lst)):
    if lst[i][0] == random_tanc and lst[i][2] == 'Vilma':
        print('Vilma', random_tanc, 'tancot', lst[i][1], '-val/vel tancolta.')
        break

for i in range(len(lst)):
    if lst[i][1] in fiuk:
         szamlalo_fiu[lst[i][1]] += 1
    else:
        fiuk.append(lst[i][1])
        szamlalo_fiu.update({lst[i][1]:1})
        
print('Fiuk: ', fiuk)



legtobbszor_fiu.append(max(szamlalo_fiu, key=szamlalo_fiu.get))
print(szamlalo_fiu)

for i in range(len(lst)):
    if lst[i][2] in lanyok:
        szamlalo_lany[lst[i][2]] += 1
    else:
        lanyok.append(lst[i][2])
        szamlalo_lany.update({lst[i][2]:1})

print('Lanyok: ', lanyok)

legtobbszor_lany.append(max(szamlalo_lany, key=szamlalo_lany.get))

#print(szamlalo_lany)
#print(szamlalo_fiu)
print('Fiu aki legtobbszor tancolt: ',legtobbszor_fiu)
print('Lany aki a legtobbszor tancolt: ',legtobbszor_lany)
