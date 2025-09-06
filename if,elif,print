#zeptam se na jmeno,vek,oblibene cislo, a na oblibenou barvu

jmeno = input("tvoje jmeno:")
vek = int(input("tvuj vek:"))
oblibene_cislo = int(input("tvoje oblibene cislo:"))
oblibena_barva = input("tvoje oblibena barva:")

#pridam oblibenemu cislo + 10 a udelam mocninu dvou
deset = oblibene_cislo + 10
mocnina2 = oblibene_cislo **2 

#podle veku zjistim pokud je dite, teenager nebo dospely (dite 0-13,teenager 13-17, dospely 18+)

if vek <= 13:
    kategorie = "dite"
elif vek < 18:
    kategorie = "teenager"
else:
    kategorie = "dospely"
#k kazde kategorii veku (dite,teenager,dospely) pridam svou individualni zpravu
if kategorie == "dite":
    zprava = "Hraj si a bav se"
elif kategorie == "teenager":
    zprava = "Zivot je zabava"
else:
    zprava = "Drz se a bud skvely"

#vypisu vsechny udaje uzivatele
print(f"Ahoj {jmeno}!Jsi {kategorie}\nTvoje oblibene cislo + 10 je {deset} a mocnina tveho oblibeneho cisla je {mocnina2} \nTvoje oblibena barva je {oblibena_barva}." )
print(f"Zprava pro tebe: {zprava}")

