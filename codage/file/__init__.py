def read_data(filepath,mode='r'):
    with open(filepath, mode) as f:
        data = f.read().strip()
    return data

# Fonction pour lire depuis un fichier binaire
def read_binary_file(filename: str):
    with open(filename, 'rb') as f:
        padding = f.read(1)[0]  # Lire le premier byte (padding)
        byte_data = f.read()
    
    binary_str = ''.join(f'{byte:08b}' for byte in byte_data)
    
    # Retirer le padding
    if padding > 0:
        binary_str = binary_str[:-padding]
    
    return binary_str


def load_huffman_data(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().strip().splitlines()
    if len(lines) < 3:
        raise ValueError("File format incorrect. Expected at least 3 lines.")
    m = int(lines[0].strip())
    alphabets = lines[1].strip().split()
    probabilities = list(map(float, lines[2].strip().split()))
    if len(alphabets) != m or len(probabilities) != m:
        raise ValueError("Mismatch between declared size and provided data.")
    return m , alphabets, probabilities

def write_huffman_dico(filePath,m,S,C):
    with open(filePath, 'w') as f:
        for i in range(m):
            f.write(f'{S[i]}:{C[i]}\n')
def load_huffman_dico(filePath):
    huffDico = dict()
    with open(filePath,'r') as f:
        lines = f.read().strip().splitlines()
    for line in lines:
        [k,v] = line.strip().split(':')
        huffDico.__setitem__(k,v)
    print(huffDico)
    return huffDico

# Fonction pour écrire dans un fichier binaire
def write_binary_file(data: str, filename: str):
    # Ajouter le padding nécessaire (nombre de bits ajoutés)
    print(data)
    padding = (8 - len(data) % 8) % 8
    padded_data = data + '0' * padding
    
    # Convertir en bytes
    byte_array = bytearray()
    for i in range(0, len(padded_data), 8):
        byte = padded_data[i:i+8]
        byte_array.append(int(byte, 2))
    
    # Écrire dans le fichier (le premier byte contient le nombre de bits de padding)
    with open(filename, 'wb') as f:
        f.write(bytearray([padding]))  # Écrire le padding en premier
        f.write(byte_array)