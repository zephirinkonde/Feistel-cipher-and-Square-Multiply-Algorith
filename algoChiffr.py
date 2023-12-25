#Zephirin_Konde
def feistel_cipher(block, permutation, left_shift, right_shift, k1, k2):
    # Appliquer la permutation donnée
    permuted_block = [block[i] for i in permutation]

    # Diviser le bloc en deux moitiés
    left_half = permuted_block[:4]
    right_half = permuted_block[4:]

    # Premier Round
    d1 = int(''.join(left_half), 2) ^ k1
    g1 = int(''.join(right_half), 2) ^ (int(''.join(left_half), 2) | k1)
    # Deuxième Round
    d2 = int(''.join(g1), 2) ^ k2
    g2 = int(''.join(d1), 2) ^ (int(''.join(g1), 2) | k2)

    # Concaténer les deux moitiés
    encrypted_block = g2 + d2

    # Appliquer l'inverse de la permutation donnée
    inverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    permuted_encrypted_block = [encrypted_block[i] for i in inverse_permutation]

    return permuted_encrypted_block

# Demander à l'utilisateur de saisir le bloc à chiffrer, la permutation, l'ordre de décalage à gauche et à droite, et les sous-clés
block = input("Entrez le bloc de longueur 8 à chiffrer : ")
permutation = input("Entrez la permutation de longueur 8 : ")
left_shift = int(input("Entrez l'ordre de décalage à gauche : "))
right_shift = int(input("Entrez l'ordre de décalage à droite : "))
k1 = int(input("Entrez la première sous-clé de longueur 4 : "), 2)
k2 = int(input("Entrez la deuxième sous-clé de longueur 4 : "), 2)

# Convertir le bloc et la permutation en listes de bits
block = [int(bit) for bit in block]
permutation = [int(bit) for bit in permutation]

# Chiffrer le bloc en utilisant les paramètres spécifiés par l'utilisateur
encrypted_block = feistel_cipher(block, permutation, left_shift, right_shift, k1, k2)

# Afficher le bloc chiffré
print("Bloc chiffré : ", ''.join([str(bit) for bit in encrypted_block]))
