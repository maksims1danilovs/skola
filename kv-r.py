a = float(input("Zadej a: "))
b = float(input("Zadej b: "))
c = float(input("Zadej c: "))

diskriminant = b**2 - 4 * a * c

if diskriminant < 0:
    print("Rovnice nema realne reseni.")

elif diskriminant == 0:
    x = -b / (2 * a)
    print(f"Dvojnasobny koren: x = {x}")

else:
    v1 = (-b + diskriminant ** 0.5) / (2 * a)
    v2 = (-b - diskriminant ** 0.5) / (2 * a)
    print(f"x1 = {v1}, x2 = {v2}")