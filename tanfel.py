tanarok=[]
tantargyak=[]
osztalyok=[]
oraszam=[]
rekord=[]

with open("beosztas.txt","r",encoding="UTF-8") as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len(rekord) == 4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszam.append(int(rekord[3]))
            rekord=[]

def osszegzes(be_tanar, oraszam, tanarok):
    osszOraszam = 0
    for i in range(len(tanarok)):
        if tanarok[i] == be_tanar:
            osszOraszam += oraszam[i]
    return osszOraszam

print("2.feladat")
print(f"A bejegyzések száma: {len(tanarok)}")
print("3.feladat")
print(f"Az iskolában a heti összóraszám: {sum(oraszam)}")
print("4.feladat")

be_tanar = input("Kérem a tanár nevét: ") or "Albatrosz Aladin"
print(f"A tanár heti óraszáma: {osszegzes(be_tanar, oraszam, tanarok)}")

def eldontes(be_osztaly, be_tantargy, tantargyak, osztalyok):
    i = 0
    while i < len(tantargyak) and not (be_tantargy == tantargyak[i] and be_osztaly.split(".")[0] == osztalyok[i].split(".")[0] and "x" in osztalyok[i]):
        i += 1    
    return i < len(tantargyak)

print("6.feladat")
be_osztaly = input("Kérem az osztályt: ") or "10.b"
be_tantargy = input("Kérem a tantárgyat: ") or "kémia"
if eldontes(be_osztaly, be_tantargy, tantargyak, osztalyok):
    print("Csoport bontásban tanulják")
else:
    print("Nem tanulnak csoportbontásban")

print("7.feladat")

def megszamoltanarok(tanarok):
    tanarokEgyedi = []
    for tanar in tanarok:
        if tanar in tanarok:
            if tanar not in tanarokEgyedi:
                tanarokEgyedi.append(tanar)
    print(tanarokEgyedi)
    return len(tanarokEgyedi)

print(f"Az iskolában {megszamoltanarok(tanarok)} tanár tanít")

tantargyak_nevei = "tantargyak.txt"
tantargy_egyedi_nevek = set(tantargyak)

with open(tantargyak_nevei, "w", encoding="utf-8") as file:
    for tantargy in tantargy_egyedi_nevek:
        file.write(tantargy + "\n")
