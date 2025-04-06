from typing import Tuple, Union
import numpy as np
import cv2

def read_image_file(filepath: str):
    """
    Read an image file using OpenCV
    
    Args:
        filepath: Path to the image file (supports BMP, JPG, PNG, etc.)
    
    Returns:
        Tuple of (image_data, metadata) or None if reading fails
        - image_data: numpy array of pixel data (height × width × channels)
        - metadata: dictionary with basic image info
    """
    try:
        # Read image (IMREAD_UNCHANGED preserves original color depth/channels)
        img = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
        
        if img is None:
            raise ValueError("OpenCV failed to read the image")
        
        # Convert BGR to RGB for color images
        if len(img.shape) == 3 and img.shape[2] == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Prepare metadata
        metadata = {
            'width': img.shape[1],
            'height': img.shape[0],
            'channels': 1 if len(img.shape) == 2 else img.shape[2],
            'dtype': str(img.dtype)
        }
        
        return img, metadata
        
    except Exception as e:
        print(f"Error reading image: {str(e)}")
        return None

import numpy as np

def convert_to_grayscale(image_path: str, method: str = 'weighted', output_path: str = None):
    """
    Convertit une image en nuances de gris avec différentes méthodes
    
    Args:
        image_path: Chemin vers l'image
        method: Méthode de conversion ('average', 'weighted', 'luminosity', 'desaturation')
        output_path: Si spécifié, sauvegarde l'image résultante
    
    Returns:
        Image en nuances de gris (numpy array)
    """
    # Charger l'image (conserve les canaux alpha si présents)
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    if img is None:
        raise ValueError("Impossible de charger l'image")
    
    # Conversion selon la méthode choisie
    if len(img.shape) == 2:  # Déjà en niveaux de gris
        gray = img
    else:
        if method == 'average':
            # Moyenne simple (R+G+B)/3
            gray = np.mean(img[..., :3], axis=2).astype(np.uint8)
        elif method == 'weighted':
            # Pondération OpenCV (BGR)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif method == 'luminosity':
            # Pondération perceptuelle (REC 601)
            weights = np.array([0.299, 0.587, 0.114])
            gray = np.dot(img[..., :3], weights).astype(np.uint8)
        elif method == 'desaturation':
            # Désaturation (max + min)/2
            max_val = np.max(img[..., :3], axis=2)
            min_val = np.min(img[..., :3], axis=2)
            gray = ((max_val + min_val) / 2).astype(np.uint8)
        else:
            raise ValueError("Méthode non reconnue")
    
    # Sauvegarde si demandé
    if output_path:
        cv2.imwrite(output_path, gray)
    
    return gray