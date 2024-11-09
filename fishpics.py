import os
from PIL import Image
import numpy as np

def load_fish_data(data_path):
    images = []
    labels = []
    
    # Iterate through each species directory
    for species in os.listdir(data_path):
        species_path = os.path.join(data_path, species)
        
        if os.path.isdir(species_path):  # Check if it's a directory
            for img_file in os.listdir(species_path):
                img_path = os.path.join(species_path, img_file)
                
                # Load the image
                try:
                    img = Image.open(img_path)
                    img = img.resize((224, 224))  # Resize to a fixed size (e.g., 224x224)
                    img_array = np.array(img)  # Convert to numpy array
                    
                    # Check if the image has the expected shape
                    if img_array.shape == (224, 224, 3):  # Assuming RGB images
                        images.append(img_array)
                        labels.append(species)  # Use the directory name as the label
                except (IOError, ValueError) as e:
                    print(f"Error loading image {img_path}: {e}")  # Log the error

    return np.array(images), np.array(labels)

# Example usage
data_path = 'fish/'
images, labels = load_fish_data(data_path)
