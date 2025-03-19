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
    