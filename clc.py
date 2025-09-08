a = float(input("zadejte prvni cislo:  "))
b = float(input("zadejte druhe cislo:  "))

operace = input("Operace (+,-,*,/):  ")


if operace == "+":
    print(a + b)
elif operace == "-":
    print(a - b)
elif operace == "*":
    print(a * b)
elif operace == "/":
    if b != 0:
        print(a / b)
    else:
        print("Delit nulou nelze")
else:
    print("Neznama operace")
    
   


