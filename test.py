from codage.file import *
from codage import *

# --- HUFFMAN DATA ----
data = read_data("assets/test/text.txt")
M,S,P = huffman_base(data)
write_huffman_data('assets/test/data.txt',M,S,P)

# ---- HUFFMAN DICO ----
C = huffman_render(M,S,P)
dico = huffman_dico(M,S,C)
write_huffman_dico('assets/test/dico.txt',M,S,C)

# # ----- HUFFMAN ENCODE -----
# source_file = read_data('assets/test/compressed.txt')
# source = source_file
# try:
#     encoded = huffman_encode(source,dico)
#     write_compressed_binary(encoded,'assets/test/compressed.bin')
# except Exception as e:
#     print(f"Cannot encoded : {source}")
#     print(e)
    
# # ----- HUFFMAN DECODE -----
# read_binary_file('assets/test/compressed.bin')
# decoded = huffman_decode(encoded,dico)
# print('--- DECODED ----')
# print(decoded)

