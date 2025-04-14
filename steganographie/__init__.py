from typing import List, Tuple
import numpy as np
import cv2
import struct


def read_wav_header(file_path):
    with open(file_path, 'rb') as f:
        # Read the first 44 bytes of the file
        header = f.read(44)
        
        # Unpack the header
        (
            chunk_id, chunk_size, format,
            subchunk1_id, subchunk1_size, audio_format,
            num_channels, sample_rate, byte_rate,
            block_align, bits_per_sample,
            subchunk2_id, subchunk2_size
        ) = struct.unpack('<4sI4s4sIHHIIHH4sI', header)
        
        header_info = {
            'chunk_id': chunk_id.decode('ascii'),
            'chunk_size': chunk_size,
            'format': format.decode('ascii'),
            'subchunk1_id': subchunk1_id.decode('ascii'),
            'subchunk1_size': subchunk1_size,
            'audio_format': audio_format,
            'num_channels': num_channels,
            'sample_rate': sample_rate,
            'byte_rate': byte_rate,
            'block_align': block_align,
            'bits_per_sample': bits_per_sample,
            'subchunk2_id': subchunk2_id.decode('ascii'),
            'subchunk2_size': subchunk2_size
        }
        
        return header_info

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

def read_audio_data(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(44)
        data = f.read()
    
    # Unpack the header to get the number of channels and bits per sample
    header_info = read_wav_header(file_path)
    # num_channels = header_info['num_channels']
    bits_per_sample = header_info['bits_per_sample']
    
    # Determine the format for unpacking the audio data
    if bits_per_sample == 16:
        fmt = '<' + 'h' * (len(data) // 2)
    elif bits_per_sample == 8:
        fmt = '<' + 'b' * len(data)
    else:
        raise ValueError("Unsupported bit depth: {}".format(bits_per_sample))
    
    # Unpack the audio data
    audio_data = struct.unpack(fmt, data)

    return (audio_data , header , fmt)

def steg_decode_wav(filepath: str, positions: List[int]) -> bytes:
    """
    Décode un message caché dans un fichier audio WAV en extrayant les bits LSB
    aux positions spécifiées.

    Args:
        filepath: Chemin vers le fichier .wav
        positions: Liste d'indices (positions d'échantillons) où sont cachés les bits

    Returns:
        Données extraites sous forme de bytes
    """
    audio_data, header, fmt = read_audio_data(filepath)
    
    bits = []
    
    for pos in positions:
        if pos >= len(audio_data):
            raise ValueError(f"Position invalide: {pos} - Taille audio: {len(audio_data)}")
        
        sample = audio_data[pos]
        
        # Si c’est signé (genre 16 bits), le convertir à positif avant d’extraire le bit
        if isinstance(sample, int):
            lsb = sample & 1
            bits.append(lsb)
            print(f"Pos {pos} | Valeur: {sample} | LSB: {lsb}")
        else:
            raise ValueError("Format inattendu dans les données audio")

    return bits_to_bytes_str(bits)
