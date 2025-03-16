
# 2024. október - Autók mozgása
# https://dload-oktatas.educatio.hu/erettsegi/feladatok_2024osz_kozep/k_digkult_24okt_fl.pdf

adatok = []

with open('C:\\Users\\jgyor\\OneDrive\\Dokumentumok\\GitHub\\Emelt_szintu_erettsegi_py\\2024_oktober\\jeladas.txt') as forrasfajl:
    for sor in forrasfajl:
        adatsor = sor.strip().split('\t')
        for index in range(1, 4):
            adatsor[index] = int(adatsor[index])
        adatok.append(adatsor)

print('2. feladat')
print(f'Az utolsó jeladás időpontja {adatok[-1][1]}:{adatok[-1][2]}, a jármű rendszáma {adatok[-1][0]}')

print('3. feladat')
keresett = adatok[0][0]
idopontok = []
for adatsor in adatok:
    if adatsor[0] == keresett:
        idopontok.append(f'{adatsor[1]}:{adatsor[2]}')
print(f'Az első jármű: {keresett}')
print('Jeladásainak időpontjai:', end=' ')
print(*idopontok, sep=' ')

print('4. feladat')
ora = 6  # int(input('Kérem, adja meg az órát: '))
perc = 54 # int(input('Kérem, adja meg a percet: '))
szamlalo = 0
for adatsor in adatok:
    if adatsor[1] == ora and adatsor[2] == perc:
        szamlalo += 1
print(f'A jeladások száma: {szamlalo}')

print('5. feladat')
max_v = max([adatsor[-1] for adatsor in adatok])
max_v_rndsz = []
for adatsor in adatok:
    if adatsor[-1] == max_v:
        max_v_rndsz.append(adatsor[0])

print(f'A legnagyobb sebesség km/h: {max_v}')
print('A járművek:', end=' ')
print(*max_v_rndsz, sep=' ')


def ora(h, p):
    return h + (p / 60)


print('6. feladat')
keresett = 'ZVJ-638' # input('Kérem, adja meg a rendszámot: ')
meresek = []
talalat = False
for adatsor in adatok:
    if adatsor[0] == keresett:
        meresek.append([adatsor[0], adatsor[1], adatsor[2], adatsor[3], 0])
        talalat = True

if talalat:
    for index in range(1, len(meresek)):
        t = ora(meresek[index][1], meresek[index][2]) - ora(meresek[index-1][1], meresek[index-1][2])
        v = meresek[index-1][3]
        s = v * t
        meresek[index][-1] = meresek[index - 1][-1] + s
    # print(*meresek, sep='\n')
    for meres in meresek:
        print(f'{meres[1]}:{meres[2]} {meres[-1]:.1f} km')
else:
    print('Nem találtam ilyen rendszámot az adatok között.')

