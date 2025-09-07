slovo = "abrakadabra"
pismeno = "z"

x = 1
y = 0
print(f"hledane pismeno je'{pismeno}'")
print(f"x je {x}")
print(f"y je {y}")

if pismeno in slovo or x==y:
    print("podminka je splnena")
else:
    print("podminka neni splnena")
