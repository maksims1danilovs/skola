age = int(input("Zadejte věk: "))


if age >= 18:
    print("Dospělý")
elif age >= 15:
    print("Dospívající")
elif age > 0:
    print("Dítě")
else:
    print("Toto číslo není věk.")

