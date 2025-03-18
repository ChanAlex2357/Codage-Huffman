import numpy as np
import pandas as pd
from codage.file.access import loadCodeData , writeHuffman
from codage import huffmanRender

print('Codage de l\'information en utilisant le codage de Huffman')
# Recuperation des donnees m, S, P
m,S,P = (loadCodeData('assets/input.txt'))
# Traitement
C = huffmanRender(m,S,P)
# Resultat
print(S)
print(C)
writeHuffman('assets/dico.txt',m,S,C)
