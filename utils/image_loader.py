import os
from PIL import Image

def load_images(folder):
    images = []
    metadata = []

    for fname in os.listdir(folder):
        if not fname.endswith(".jpeg"): # GET ALL IMAGES THAT ARE JPEG
            continue

        date = fname.split("_")[0]  # YYYY-MM-DD
        path = os.path.join(folder, fname)

        img = Image.open(path).convert("RGB") # SAVE THE IMAGES TO PATH IN RGB FORMAT
        images.append(img) # LIST OF IMAGES
        metadata.append(date) # TIMESTAMPS/ FILENAMES/ METADATA

    return images, metadata

