lst = open('Digitalis_kultura\\2024_oktober_eng\\felszin_tpont.txt','r').read().split('\n')

#print(lst)

for i in range(len(lst)):
    lst[i] = lst[i].split('\t')

#print(lst)

dict = {}

for i in range(len(lst)):
    dict.update({lst[i][3]:{'kozeppont':float(lst[i][0]),'x':float(lst[i][1]),'y':float(lst[i][2])}})
                
print(dict)

print('2.feladat')

print(f'A kraterek szama: {len(dict)}')