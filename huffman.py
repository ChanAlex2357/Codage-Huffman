import numpy as np
import pandas as pd
from codage.file import loadHuffmanData , writeHuffmanDico
from codage import huffmanRender

print('Codage de l\'information en utilisant le codage de Huffman')
# Recuperation des donnees m, S, P
m,S,P = (loadHuffmanData('assets/input.txt'))
# Traitement
C = huffmanRender(m,S,P)
# Resultat
print(S)
print(C)
writeHuffmanDico('assets/dico.txt',m,S,C)
