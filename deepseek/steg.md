Voici une implémentation complète de la stéganographie pour images en niveaux de gris (sans librairie externe), structurée selon vos exigences :

### 1. Lecture brute d'un fichier image (nuances de gris)
```python
def read_gray_image_file(filepath: str) -> bytearray:
    """Lit un fichier image BMP 8-bit (nuances de gris) sans librairie"""
    with open(filepath, 'rb') as f:
        data = bytearray(f.read())
    
    # Vérification du format BMP 8-bit (header simplifié)
    if data[0] != 0x42 or data[1] != 0x4D:
        raise ValueError("Format non supporté: Seul BMP 8-bit est accepté")
    
    # Extraction des données pixels (offset 0x36 pour BMP 8-bit)
    pixel_offset = int.from_bytes(data[10:14], 'little')
    return data[pixel_offset:]
```

### 2. Extraction des bits depuis les positions
```python
def steg_gray_image_bytes(img_bytes: bytearray, bit_positions: list) -> list:
    """
    Récupère les bits LSB aux positions spécifiées
    Args:
        img_bytes: Données brutes de l'image
        bit_positions: Liste de tuples (byte_offset, bit_offset)
                      bit_offset [0-7] (0=LSB, 7=MSB)
    Returns:
        Liste des bits extraits (0 ou 1)
    """
    extracted_bits = []
    for byte_off, bit_off in bit_positions:
        byte = img_bytes[byte_off]
        bit = (byte >> bit_off) & 1
        extracted_bits.append(bit)
    return extracted_bits
```

### 3. Décodage des données binaires
```python
def steg_decode_gray_image(img_bytes: bytearray, bit_positions: list) -> bytes:
    """Reconstruit les bytes cachés à partir des positions"""
    bits = steg_gray_image_bytes(img_bytes, bit_positions)
    
    # Conversion des bits en bytes
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:
            break  # Padding implicite avec des 0
        byte = sum(bit << idx for idx, bit in enumerate(byte_bits))
        byte_array.append(byte)
    
    return bytes(byte_array)
```

### 4. Fonction complète de décodage
```python
def steg_decode_gray_image_file(filepath: str, bit_positions: list) -> bytes:
    """Lit et décode un fichier image en une étape"""
    img_bytes = read_gray_image_file(filepath)
    return steg_decode_gray_image(img_bytes, bit_positions)
```

### Exemple d'utilisation
```python
# Configuration des positions (exemple simplifié)
positions = [
    (0, 0),  # Premier byte, LSB
    (0, 1),  # Premier byte, 2e bit
    (1, 0),  # Deuxième byte, LSB
    # ...
]

# Décodage
hidden_data = steg_decode_gray_image_file("secret.bmp", positions)
print(f"Message extrait: {hidden_data.decode('utf-8', errors='ignore')}")
```

### Structure du flux de données
```
Fichier BMP
├── Header (54 bytes)
└── Données pixels
    ├── Byte 0: [bit7][bit6][bit5][bit4][bit3][bit2][bit1][LSB] ← bit_positions=(0,0)
    ├── Byte 1: [...]
    └── ...
```

### Points clés :
1. **Format supporté** : BMP 8-bit (nuances de gris) uniquement
2. **Optimisations** :
   - Accès direct aux bytes sans conversion d'image
   - Gestion efficace de la mémoire avec `bytearray`
3. **Flexibilité** :
   - Positions spécifiables au niveau bit près
   - Extensible pour ajouter un header de métadonnées

Pour étendre ce système :
- Ajouter un marqueur de début/fin de message
- Implémenter un chiffrement des données extraites
- Gérer le padding des bits de fin automatiquement