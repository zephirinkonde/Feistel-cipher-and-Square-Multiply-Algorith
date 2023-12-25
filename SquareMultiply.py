from cgitb import reset
#Zephirin_Konde_Umba

def square_multiply(base, exp, mod):
    b = bin(exp)[2:]
    res = 1
    for i in b :
        res = res ** 2 % mod
        if i == '1':
           res = res * base % mod
    return res

#Demande à l'utilisateur d'enter les valeurs 
base = int(input("Entrez la valeur de la base :"))
exp = int(input("Entrez l'exposant :"))
mod = int(input("Entrez le modulo :"))

# Calcul de la valeur avec l'algorithme Square Multiply
result = square_multiply(base, exp, mod)

# Affichage du résultat

print(f"Le résultat de {base}^{exp} mod {mod} est : {result}")