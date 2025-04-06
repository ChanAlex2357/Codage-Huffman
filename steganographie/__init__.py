from typing import List, Tuple
import numpy as np
import cv2

def read_image_file(filepath: str) -> Tuple[np.ndarray, dict]:
    """Lit une image avec OpenCV et retourne les données et métadonnées"""
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Impossible de charger l'image: {filepath}")
    
    metadata = {
        'width': img.shape[1],
        'height': img.shape[0],
        'channels': 1,
        'dtype': str(img.dtype)
    }
    return img, metadata

def get_lsb_bits_from_positions(img_array: np.ndarray, positions: List[Tuple[int, int]]) -> List[int]:
    """
    Extrait les bits LSB aux positions spécifiées dans une image en niveaux de gris
    et affiche la représentation binaire complète des pixels
    
    Args:
        img_array: Tableau numpy 2D de l'image (hauteur × largeur)
        positions: Liste de tuples (row, col) spécifiant les positions des pixels
    
    Returns:
        Liste des bits LSB (0 ou 1) dans l'ordre spécifié
    """
    bits = []
    height, width = img_array.shape
    
    for row, col in positions:
        if row >= height or col >= width:
            raise ValueError(f"Position invalide: ({row}, {col}) - Image size: {height}x{width}")
        
        pixel_value = img_array[row, col]
        # Conversion en binaire sur 8 bits (avec padding)
        binary_str = format(pixel_value, '08b')
        lsb = pixel_value & 1  # Extraire le bit le moins significatif
        bits.append(lsb)
        
        # Debug print avec représentation binaire
        print(f"Position ({row}, {col})")
        print(f"Valeur décimale: {pixel_value}")
        print(f"Valeur binaire: {binary_str} (LSB: {binary_str[7]})")
        print("-" * 30)
    
    return bits

def bits_to_bytes_str(bits: List[int]) -> bytes:\
    return ''.join([f'{i}' for i in bits])

def bits_to_bytes(bits: List[int]) -> bytes:
    """
    Convertit une liste de bits en bytes
    Args:
        bits: Liste de bits (0 ou 1)
    Returns:
        Bytes reconstitués
    """
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:
            # Compléter avec des 0 si nécessaire
            byte_bits += [0] * (8 - len(byte_bits))
        byte = sum(bit << pos for pos, bit in enumerate(byte_bits))
        byte_array.append(byte)
    return bytes(byte_array)

def steg_decode_gray_image_file(filepath: str, positions: List[Tuple[int, int]]) -> bytes:
    """
    Décode un message caché dans une image en niveaux de gris
    
    Args:
        filepath: Chemin vers l'image
        positions: Liste de tuples (row, col) spécifiant où les bits sont cachés
    
    Returns:
        Données extraites sous forme de bytes
    """
    # 1. Charger l'image
    img_array, _ = read_image_file(filepath)
    
    # 2. Extraire les bits LSB
    bits = get_lsb_bits_from_positions(img_array, positions)

    # 3. Convertir en bytes
    decoded_data = bits_to_bytes_str(bits)

    return decoded_data