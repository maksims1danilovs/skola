# >>> zde nastavujte hodnoty
rychlost = 60
#lokace = "dálnice"
#lokace = "mimo_obec"
lokace = "obec"

# >>> tento řádek neměňte
print("Pozice auta:", lokace, "\nRychlost:", rychlost)

# >>> TODO: zde napište svůj kód

dalnice_limit = 130
mimo_obec_limit = 90
obec_limit = 50

if lokace == "dálnice":
    if rychlost <= dalnice_limit:
        print("OK")
    else:
        print("Vysoka rychlost")

if lokace == "mimo_obec":
    if rychlost <= mimo_obec_limit:
        print("OK")
    else:
        print("Vysoka rychlost")

        
if lokace == "obec":
    if rychlost <= obec_limit:
        print("OK")
    else:
        print("Vysoka rychlost")
        