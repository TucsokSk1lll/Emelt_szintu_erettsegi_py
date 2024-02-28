x = open(file="2023_majus\\kep.txt", mode="r")
x = x.read()
print(x)
x = x.split(" ")

lst = [ ]

for i in range(0,len(x)-3,3):
    y = [ ]
    for j in range(3):
        y.append(x[i+j])
    lst.append(y)

#print(lst)