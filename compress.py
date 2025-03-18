from codage.file import loadHuffmanDico , readData

# Recuperer des donnees : le dictionnaire huffman et le donnee a compresse
huffDico = loadHuffmanDico('assets/dico.txt')
data = readData('assets/compress.txt')