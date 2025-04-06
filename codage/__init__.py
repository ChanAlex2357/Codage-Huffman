from .huffman.HuffmanTree import HuffmanTree
from .huffman.HuffmanForest import HuffmanForest
from typing import List

def build_huffman_forest(m,S,P):
    trees = []
    for i in range(m):
        trees.append(build_huffman_tree(S[i],P[i]))
    return HuffmanForest(trees)

def build_huffman_tree(Si,Pi):
    return (HuffmanTree(Si,Pi))

def merge_trees(trees: List[HuffmanTree], m: int) -> List[HuffmanTree]:
    if m == 1:
        return trees
    # Trier dans l'ordre décroissant
    trees.sort(key=lambda tree: tree.get_probabilite(), reverse=True)
    # Extraire les mins
    t1 = trees[-2]
    t2 = trees[-1]
    # Fusionner les 2 mins
    mergedTree = HuffmanTree(
        libelle= t1.get_libelle()+t2.get_libelle(),
        probabilite= t1.get_probabilite()+t2.get_probabilite(),
        tree1=t1,
        tree2=t2
    )
    # Cree une copy pour ne pas detruire le tableau original
    new_T = trees.copy()
    new_T = trees[:m-2] + [mergedTree]
    # Descente dans l'arbre
    rT = merge_trees(new_T, m-1)
    # Remonter l'arbrer pour cree le code
    merge = []
    for rt in rT:
        if rt.get_tree1() == None and rt.get_tree2() == None:
            merge += [rt]
            continue
        rt.get_tree1().set_code(rt.get_code() + '1')
        rt.get_tree2().set_code(rt.get_code() + '0')
        merge += [rt.get_tree1()]
        merge += [rt.get_tree2()]
    return merge
        
def get_binaries(encoded):
    binary_list = [f'{byte:08b}' for byte in encoded]
    return binary_list

def get_binaries_str(encoded):
    binary_str = ''.join(f'{byte:08b}' for byte in encoded)
    return binary_str

def render_forest(forest,m):
    trees = forest.get_trees()
    merge_trees(trees,m)

def huffman_render(m,S,P):
    forest  = build_huffman_forest(m,S,P)
    render_forest(forest,m)
    C = []
    for tree in forest.get_trees():
        C.append(tree.get_code())
    return C 

# Fonction de décodage Huffman
def huffman_decode(encoded: str, dico: dict):
    # Inverser le dictionnaire pour décodage
    reverse_dict = {v: k for k, v in dico.items()}
    
    decoded = []
    current_code = ""
    
    for bit in encoded:
        current_code += bit
        if current_code in reverse_dict:
            decoded.append(reverse_dict[current_code])
            current_code = ""
    
    if current_code:
        raise ValueError("Encodage invalide - bits restants non décodés")
    
    return ''.join(decoded)

def huffman_encode_word(mot, huffman_dict):  
    # Encodage du mot
    encoded_data = ''
    try:
        encoded_data = ''.join([huffman_dict[char] for char in mot])
    except Exception as e:
        print(e)
    return encoded_data


def huffman_encode(sentence, huffman_dict):
    encoded = ''.join([huffman_encode_word(mot,huffman_dict) for mot in sentence])
    return encoded

def huffman_dico(m,s,c):
    '''
        Crée un dictionnaire de Huffman à partir des mots et de leurs codes
        Params :
            - m : le nombre de mots
            - s : la liste des mots
            - c : la liste des codes de Huffman
        Returns :
            - dico : le dictionnaire de Huffman
    '''
    dico = {}
    for i in range(m):
        dico[s[i]] = c[i]
    return dico
from collections import Counter
import re

import re
from collections import Counter

def huffman_base(text, keep_spaces=True):

    if keep_spaces:
        # # Supprime la ponctuation mais conserve les espaces
        # text = re.sub(r'[^\w\s]', '', text)
        # Remplace les espaces multiples par un seul espace
        text = re.sub(r'\s+', ' ', text).strip()
    else:
        # Supprime tout sauf lettres et chiffres (y compris les espaces)
        text = re.sub(r'[^\w]', '', text)

    # Calcul du nombre total de caractères (y compris espaces si keep_spaces=True)
    total_caracteres = len(text)
    
    if total_caracteres == 0:
        return 0, [], []

    # Comptage des occurrences de chaque caractère (y compris espace)
    freq = Counter(text)

    # Caractères triés
    caracteres_tries = sorted(freq.keys())

    # Probabilités dans le même ordre
    p = [freq[char] / total_caracteres for char in caracteres_tries]

    m = len(p)  # nombre de caractères différents

    return m, caracteres_tries, p


# def huffman_base_words(text):
#     text = re.sub(r'[^\w\s]', '', text)  # Enlève tout sauf les lettres, chiffres et espaces
    
#     # Séparation des mots
#     mots = text.split()
    
#     if not mots:
#         return 0, [], []
    
#     # Calcul du nombre total de mots (pas de lettres)
#     total_mots = len(mots)
    
#     # Comptage des occurrences de chaque mot
#     freq = Counter(mots)
    
#     # Mots distincts triés
#     mots_distincts = sorted(freq.keys())
    
#     # Probabilités dans le même ordre
#     probabilites = [freq[word]/total_mots for word in mots_distincts]
    
#     # Nombre de mots distincts
#     m = len(mots_distincts)
    
#     return m, mots_distincts, probabilites