import torch
import numpy as np
from utils.image_loader import load_images # LOADS IMAGES
from utils.preprocessing import transform # RESIZES AND NORMALIZES IMAGES
from models.farnet_backbone import FaRNetBackbone # FROZEN RESNET-50 FEATURE EXTRACTER

device = "cuda" if torch.cuda.is_available() else "cpu" # USE GPU IF AVAILABLE OR FALLBACK TO CPU
model = FaRNetBackbone().to(device) # INITIATES MODEL
model.eval() # DISABLES DROP OUT LAYERS AND FIXES BATCH NORMALIZATION FOR EVALUATION

def extract(folder, out_file):
    images, dates = load_images(folder)
    features = []

    for img in images:
        x = transform(img).unsqueeze(0).to(device) # UNSQUEEZE CHANGES THE DIMENSION OF THE TENSOR TO 3D (ADDS BATCH DIMENSION)
        with torch.no_grad():
            emb = model(x)
        features.append(emb.cpu().numpy()[0]) # STORES EMBEDDINGS AND REMOVES BATCH DIMENSION (1, 2048)

    np.save(out_file, np.array(features)) # (2048,)
    return dates

india_dates = extract("data/indian_images", "features/india_embeddings_clean.npy")
west_dates  = extract("data/global_images",  "features/west_embeddings_clean.npy")
