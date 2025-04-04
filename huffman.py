import numpy as np
import pandas as pd
from codage.file import load_huffman_data , write_huffman_dico
from codage import huffman_render

print('Codage de l\'information en utilisant le codage de Huffman')
# Recuperation des donnees m, S, P
m,S,P = (load_huffman_data('assets/input.txt'))
# Traitement
C = huffman_render(m,S,P)
# Resultat
print(S)
print(C)
write_huffman_dico('assets/dico.txt',m,S,C)
