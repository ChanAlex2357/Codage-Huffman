from steganographie import *
# Positions où les données sont cachées (doivent correspondre à l'encodage)
positions = [
    (10, 20, 0),  # Bit 0 encodé dans le canal R du pixel (10,20)
    (10, 21, 2),  # Bit 1 encodé dans le canal B du pixel (10,21)
]

# Décoder les données
hidden_data = steg_decode_img("assets/img/baobab.jpg", positions)
print(f"Données extraites: {hidden_data}")