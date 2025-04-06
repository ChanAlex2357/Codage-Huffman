from codage.file import *
from codage import *

data = read_data('assets/base_text.txt')
m, s, p = huffman_base(data)
print(f"Nombre total de mots (m): {m}")
print(f"\nListe des mots uniques (s): {s}")

print(p)
write_huffman_data('assets/huffman_data.txt', m, s, p)