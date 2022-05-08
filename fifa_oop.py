class Fifa:
    def __init__(self,sor):
        csapat,helyezes,valtozas,pontszam = sor.strip().split(';')
        self.csapat = csapat
        self.helyezes = int(helyezes)
        self.valtozas = int(valtozas)
        self.pontszam = int(pontszam)
#2
with open('fifa.txt', encoding=('latin2'))as f:
    fejlec = f.readline()
    lista = [Fifa(sor) for sor in f]
#3
print(f'3. feladat: A világranglistán {len(lista)} csapat szerepel')
#4
osszpontszam = 0
for sor in lista:
    osszpontszam += sor.pontszam 
print(f'4. feladat: a csapatok átlagos pontszama {"%.2f" % (osszpontszam/len(lista))}')
#5
valtozas = max(lista, key=lambda x:x.valtozas)
print(f"5. feladat: A legtöbbet javító csapat: \n\tHelyezés: {valtozas.helyezes} \n\tCsapat: {valtozas.csapat} \n\tPontszám: {valtozas.pontszam}")
#6
if 'Magyarország' in [sor.csapat for sor in lista]:
    print('6. feladat: A csapatok közt van Magyarorszag')
else:
    print('6. feladat: A csapatok közt nincs Magyarorszag')
#7
print('7. feladat: Statisztika')
szotar = {}
for sor in lista:
    szotar[sor.valtozas]=szotar.get(sor.valtozas,0)+1
for index,i in szotar.items():
    if i>1:
        print(f"{index} helyet változott csapat: {i} csapat")