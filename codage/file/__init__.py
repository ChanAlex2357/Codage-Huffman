def readData(filepath):
    with open(filepath, 'r') as f:
        data = f.read().strip()
    return data
def loadHuffmanData(filepath):
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

def writeHuffmanDico(filePath,m,S,C):
    with open(filePath, 'w') as f:
        for i in range(m):
            f.write(f'{S[i]}:{C[i]}\n')
def loadHuffmanDico(filePath):
    huffDico = dict()
    with open(filePath,'r') as f:
        lines = f.read().strip().splitlines()
    for line in lines:
        [k,v] = line.strip().split(':')
        huffDico.__setitem__(k,v)
    print(huffDico)
    return huffDico
