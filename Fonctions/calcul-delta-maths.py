from math import sqrt

a = float(input("Saisir la valeur de [a] ")) #-6
b = float(input("Saisir la valeur de [b] ")) #110
c = float(input("Saisir la valeur de [c] ")) #-210

# print(a + b + c, "\n")

# Calcul de delta
delta = b * b - 4 * a * c

print("\nDelta est égal à " + str(delta),"\n")
# Si delta est inférieur alors fait cela
if delta < 0:
    print("Delta est inferieur à 0, donc pas de solution")
# ou cela
elif delta == 0:
    print("Delta égal à 0")
    result = (-b / 2 * a)
    print("x1 = x2 =",result)
# sinon fait cela
else:
    print('Delta est superieur à 0\n')
    result = (b * b - 4 * a * c)
    #print(result)
    racine_carre = sqrt(result)
    x1 = (-b + racine_carre) / (2 * -a)
    print("x1 =", x1)
    x2 = (-b - racine_carre) / (2 * -a)
    print("x2 =", x2)