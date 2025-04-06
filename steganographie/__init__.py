from PIL import Image
import numpy as np

def steg_decode_img(image_path: str, positions: list) -> bytes:
    """
    Récupère les données cachées dans une image à partir des positions spécifiées.
    
    Args:
        image_path: Chemin vers l'image contenant les données cachées
        positions: Liste des positions (x,y,canal) où les bits sont encodés
                  Format: [(x1,y1,canal1), (x2,y2,canal2), ...]
                  canal: 0=R, 1=G, 2=B
    
    Returns:
        bytes: Données binaires extraites
    """
    # Charger l'image et convertir en tableau numpy
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Extraire les bits LSB dans l'ordre des positions
    extracted_bits = []
    for x, y, channel in positions:
        pixel_value = pixels[y, x][channel]  # Accès: [y,x] car numpy est row-major
        lsb = pixel_value & 1  # Récupère le bit de poids faible (LSB)
        extracted_bits.append(str(lsb))
    
    # Convertir les bits en bytes
    binary_str = ''.join(extracted_bits)
    byte_array = bytearray()
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8].ljust(8, '0')
        byte_array.append(int(byte, 2))
    
    return bytes(byte_array)