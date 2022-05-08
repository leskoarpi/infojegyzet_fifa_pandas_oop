import pandas as pd
#2
df = pd.read_csv('fifa.txt', encoding='latin2',sep=';')
#3
print(f'3. feladat: A világranglistán {df["Csapat"].count()} csapat szerepel.')
#4
print(f'4. feladat: A csapatok átlagos pontszáma: {"%.2f" % df["Pontszam"].mean()}')
#5
print(f'5. feladat: a legtöbbet javító csapat:')
for i in df.index:
    if df["Valtozas"][i] == df['Valtozas'].max():
        print(f'\t Helyezés: {df["Helyezes"][i]}')
        print(f'\t Csapat: {df["Csapat"][i]}')
        print(f'\t Pontszám: {df["Pontszam"][i]}')
#6
if "Magyarország" in df['Csapat'].values:
    print('6. feladat: A csapatok közt van Magyarorszag')
else:
    print('6. feladat: A csapatok közt nincs Magyarorszag')
#7
print('7. feladat: Statisztika')
for i in set(df['Valtozas']):
    if sum(df["Valtozas"] == i) > 1:
        print(f'\t {i} helyet változtatott {sum(df["Valtozas"] == i)} csapat')
