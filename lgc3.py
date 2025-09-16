x = y = [1, "text", True, [1, 2, 3]]
a = 10
b = 7

slovo = "abrakadabra"
pismeno = "z"

promenna = (pismeno in slovo) or (x == y) or (x is y) and ((a+b) > 15)


if promenna:
    print("Podminka je splnena")
else:
    print("Podminka neni splnena")
