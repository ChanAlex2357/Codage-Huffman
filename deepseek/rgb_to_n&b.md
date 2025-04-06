Voici une fonction pour convertir une image en nuances de gris en utilisant différentes méthodes, avec OpenCV et sans OpenCV :

### Avec OpenCV (recommandé)
```python
import cv2
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
```

### Sans OpenCV (pure Python)
```python
from PIL import Image

def convert_to_grayscale_pil(image_path: str, method: str = 'luminosity', output_path: str = None):
    """
    Version sans OpenCV utilisant PIL/Pillow
    """
    img = Image.open(image_path)
    
    if img.mode == 'L':
        return np.array(img)  # Déjà en niveaux de gris
    
    if method == 'average':
        gray = img.convert('L')  # Méthode par défaut de PIL (similaire à 'average')
    else:
        # Conversion personnalisée
        rgb = img.convert('RGB')
        pixels = np.array(rgb)
        
        if method == 'luminosity':
            weights = np.array([0.299, 0.587, 0.114])
            gray = np.dot(pixels[..., :3], weights).astype(np.uint8)
        elif method == 'desaturation':
            max_val = np.max(pixels[..., :3], axis=2)
            min_val = np.min(pixels[..., :3], axis=2)
            gray = ((max_val + min_val) / 2).astype(np.uint8)
        else:
            raise ValueError("Méthode non supportée sans OpenCV")
    
    gray_img = Image.fromarray(gray)
    
    if output_path:
        gray_img.save(output_path)
    
    return gray
```

### Exemple d'utilisation
```python
# Avec OpenCV
gray_img = convert_to_grayscale('couleur.jpg', method='luminosity', output_path='gris.jpg')

# Sans OpenCV
gray_img_pil = convert_to_grayscale_pil('couleur.jpg', method='luminosity')
```

### Méthodes disponibles :
1. **weighted** (par défaut) : Pondération perceptuelle (0.299R + 0.587G + 0.114B)
2. **luminosity** : Identique à weighted (standard REC 601)
3. **average** : Moyenne simple (R+G+B)/3
4. **desaturation** : (Max(R,G,B) + Min(R,G,B))/2

### Notes :
- La méthode `weighted` (OpenCV) est généralement la plus naturelle visuellement
- Pour installer les dépendances :
  ```bash
  pip install opencv-python numpy pillow
  ```
- Les images en sortie sont codées sur 8 bits (niveaux 0-255)