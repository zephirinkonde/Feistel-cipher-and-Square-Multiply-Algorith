#Zephirin_Konde
def feistel_decipher(block, permutation, left_shift, right_shift, k1, k2):
    # Appliquer l'inverse de la permutation donnée
    inverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    permuted_block = [block[i] for i in inverse_permutation]

    # Diviser le bloc en deux moitiés
    left_half = permuted_block[:4]
    right_half = permuted_block[4:]

    # Deuxième Round
    g1 = int(''.join(right_half), 2) ^ k2
    d1 = int(''.join(left_half), 2) ^ (int(''.join(g1), 2) | k2)
    # Premier Round
    g0 = int(''.join(d1), 2) ^ k1
    d0 = int(''.join(g1), 2) ^ (int(''.join(g0), 2) | k1)

    # Concaténer les deux moitiés
    decrypted_block = g0 + d0

    # Appliquer l'inverse de la permutation donnée
    inverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    permuted_decrypted_block = [decrypted_block[i] for i in inverse_permutation]

    return permuted_decrypted_block

# Demander à l'utilisateur de saisir le bloc à déchiffrer, la permutation, l'ordre de décalage à gauche et à droite, et les sous-clés
block = input("Entrez le bloc de longueur 8 à déchiffrer : ")
permutation = input("Entrez la permutation de longueur 8 : ")
left_shift = int(input("Entrez l'ordre de décalage à gauche : "))
right_shift = int(input("Entrez l'ordre de décalage à droite : "))
k1 = int(input("Entrez la première sous-clé de longueur 4 : "), 2)
k2 = int(input("Entrez la deuxième sous-clé de longueur 4 : "), 2)

# Convertir le bloc et la permutation en listes de bits
block = [int(bit) for bit in block]
permutation = [int(bit) for bit in permutation]

# Déchiffrer le bloc en utilisant les paramètres spécifiés par l'utilisateur
decrypted_block = feistel_decipher(block, permutation, left_shift, right_shift, k1, k2)

# Afficher le bloc déchiffré
print("Bloc déchiffré : ", ''.join([str(bit) for bit in decrypted_block]))
