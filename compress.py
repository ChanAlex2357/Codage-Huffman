from codage.file import loadHuffmanDico, readData

# Récupérer des données : le dictionnaire Huffman et les données à compresser
huffDico = loadHuffmanDico('assets/dico.txt')
data = readData('assets/compress.txt')

encoded_data = ""

# Encoder les données en utilisant le dictionnaire Huffman
for char in data:
    if char in huffDico:
        encoded_data += huffDico[char]
    else:
        raise ValueError(f"Character '{char}' not found in Huffman dictionary")


while len(encoded_data) % 8 != 0:
    encoded_data += '0'

# Convertir la chaîne binaire en bytes
byte_array = bytearray()
for i in range(0, len(encoded_data), 8):
    byte = encoded_data[i:i+8]
    byte_array.append(int(byte, 2))

# Écrire les données compressées dans un fichier
with open('assets/compressed.bin', 'wb') as f:
    f.write(byte_array)

print("Compression terminée et données écrites dans 'assets/compressed.txt'.")
