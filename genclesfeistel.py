#ALGORITHME POUR LA GENERATION DES CLES DE FEISTEL
#BY ZEPHIRIN KONDE UMBA

def feistel_key_generation(key, permutation, left_shift, right_shift):
    # Appliquer la permutation donnée
    permuted_key = [key[i] for i in permutation]

    # Diviser la clé en deux moitiés
    k1 = permuted_key[:4]
    k2 = permuted_key[4:]

    # Appliquer les opérations XOR et AND
    k1 = int(''.join(k1), 2) ^ int(''.join(k2), 2)
    k2 = int(''.join(k2), 2) & int(''.join(k1), 2)

    # Appliquer les décalages à gauche et à droite
    for _ in range(left_shift):
        k1 = k1[1:] + [k1[0]]
    for _ in range(right_shift):
        k2 = [k2[-1]] + k2[:-1]

    # Convertir les sous-clés en chaînes de caractères binaires de longueur 4
    k1 = format(k1, '04b')
    k2 = format(k2, '04b')

    return k1, k2

# Demander à l'utilisateur de saisir la clé, la permutation, l'ordre de décalage à gauche et à droite
key = input("Entrez la clé de longueur 8 : ")
permutation = input("Entrez la permutation de longueur 8 : ")
left_shift = int(input("Entrez l'ordre de décalage à gauche : "))
right_shift = int(input("Entrez l'ordre de décalage à droite : "))

# Convertir la clé et la permutation en listes de bits
key = [int(bit) for bit in key]
permutation = [int(bit) for bit in permutation]

# Générer les sous-clés de Feistel
k1, k2 = feistel_key_generation(key, permutation, left_shift, right_shift)

# Afficher les sous-clés générées
print("Sous-clé 1 : ", k1)
print("Sous-clé 2 : ", k2)