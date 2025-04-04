from codage.file import read_byte_file , load_huffman_dico
from codage import get_binaries_str , huffman_decode

encoded = read_byte_file('assets/compressed.bin')
binary_str = get_binaries_str(encoded)
huffman_dico = load_huffman_dico('assets/dico.txt')

decoded = huffman_decode(binary_str,huffman_dico)
print('--- DECODED ----')
print(decoded)