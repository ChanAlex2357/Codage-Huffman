from steganographie import *
# Positions où les données sont cachées (doivent correspondre à l'encodage)
positions = [
    (10, 20, 0),  # Bit 0 encodé dans le canal R du pixel (10,20)
    (10, 21, 2),  # Bit 1 encodé dans le canal B du pixel (10,21)
]
# CONVERSION TN N&B
# gray_img = convert_to_grayscale('assets/img/baobab.jpg', method='luminosity', output_path='assets/img/baobab-1.jpg')

# READ IMAGE DATA
image_data,metadata = read_image_file("assets/img/baobab-1.jpg")
if image_data is not None:
    print("Image loaded successfully!")
    print(f"Dimensions: {metadata['width']}x{metadata['height']}")
    print(f"Channels: {metadata['channels']}")
    print(f"Data type: {image_data.dtype}")
    
    # For grayscale images (2D array)
    if len(image_data.shape) == 2:
        print(f"Pixel at (0,0): {image_data[0,0]}")
    # For color images (3D array)
    else:
        print(f"Pixel at (0,0): {image_data[0,0,:]}")
        
