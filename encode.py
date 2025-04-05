from codage.file import load_huffman_dico, read_data, write_binary_file
from codage import huffman_encode
# Récupérer des données : le dictionnaire Huffman et les données à compresser
huffDico = load_huffman_dico('assets/dico.txt')
data = read_data('assets/compress.txt')

# Compression
encoded = huffman_encode(data, huffDico, 'assets/compressed.bin')
write_binary_file(encoded, 'assets/compressed.bin')
print("Compression terminée et données écrites dans 'assets/compressed.bin'.")
