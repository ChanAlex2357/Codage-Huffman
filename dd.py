# Dictionnaire de codage Huffman
huffman_dict = {
    'a': '11',
    'b': '01',
    'c': '101',
    'd': '100',
    'e': '001',
    'f': '000'
}

# Mot à encoder
mot = "abcdefababc"

# Fonction pour lire depuis un fichier binaire
def read_binary_file(filename: str):
    with open(filename, 'rb') as f:
        padding = f.read(1)[0]  # Lire le premier byte (padding)
        byte_data = f.read()
    
    binary_str = ''.join(f'{byte:08b}' for byte in byte_data)
    
    # Retirer le padding
    if padding > 0:
        binary_str = binary_str[:-padding]
    
    return binary_str


# Lire le fichier compressé
read_data = read_binary_file('assets/compressed.bin')
print(f"Read data: {read_data}")

# Fonction de décodage Huffman
def huffman_decode(encoded: str, dico: dict):
    # Inverser le dictionnaire pour décodage
    reverse_dict = {v: k for k, v in dico.items()}
    
    decoded = []
    current_code = ""
    
    for bit in encoded:
        current_code += bit
        if current_code in reverse_dict:
            decoded.append(reverse_dict[current_code])
            current_code = ""
    
    if current_code:
        raise ValueError("Encodage invalide - bits restants non décodés")
    
    return ''.join(decoded)

# Décoder les données
decoded_mot = huffman_decode(read_data, huffman_dict)
print(f"Mot décodé: {decoded_mot}")
print(f"Mot original et décodé sont identiques: {mot == decoded_mot}")