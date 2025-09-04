rychlost = int(input("Vase rychlost: "))

print("1. dalnice \n2. mimo obec \n3. obec")
lokace = int(input("Zadejte cislo lokace: "))

# >>> TODO: zde napište svůj kód
rychlost_obec = 50
rychlost_mimo_obec = 90
rychlost_dalnice = 130

if lokace == 1:
    print("Pozice auta:dalnice")
    if rychlost <= rychlost_dalnice:
        print("OK")
    else:
        print("Vysoka rychlost")
    



elif lokace== 2:
    print("Pozice auta:mimo obec")
    if rychlost <= rychlost_mimo_obec:
        print("OK")
    else:
        print("Vysoka rychlost")



elif lokace== 3:
    print("Pozice auta:obec")
    if rychlost <= rychlost_obec:
        print("OK")
    else:
        print("Vysoka rychlost")

