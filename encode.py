from codage.file import load_huffman_dico, read_data, write_compressed_binary
from codage import huffman_encode
# Récupérer des données : le dictionnaire Huffman et les données à compresser
huffDico = load_huffman_dico('assets/dico.txt')
data = read_data('assets/compress.txt')

# Compression
encoded = huffman_encode(data, huffDico)
write_compressed_binary(encoded, 'assets/compressed.bin')
print("Compression terminée et données écrites dans 'assets/compressed.bin'.")


# -------- TEST TExt