from codage.file import read_binary_file, load_huffman_dico
from codage import huffman_decode

binary_str = read_binary_file('assets/compressed.bin')
huffman_dico = load_huffman_dico('assets/dico.txt')

decoded = huffman_decode(binary_str,huffman_dico)

print('--- DECODED ----')
print(decoded)