import os
import numpy as np
from datetime import datetime, date
from PIL import Image, ImageFile
import torch
from torchvision import models, transforms

ImageFile.LOAD_TRUNCATED_IMAGES = True

IMAGE_DIR = "data/indian_images"
OUTPUT_PATH = "features/indian_data.npz"

# Pretrained model (ResNet50 example)
model = models.resnet50(weights="IMAGENET1K_V1")
model.fc = torch.nn.Identity()
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

embeddings = []
dates = []

for filename in sorted(os.listdir(IMAGE_DIR)):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    # 🔑 Extract date from filename: YYYY-MM-DD_x.jpg
    date_str = filename.split("_")[0]
    img_date = datetime.strptime(date_str, "%Y-%m-%d").date()

    if img_date < date(2023, 1, 1):
        continue

    img_path = os.path.join(IMAGE_DIR, filename)
    try:
        image = Image.open(img_path).convert("RGB")
    except Exception as e:
        print(f"⚠ Skipping corrupt image: {filename}")
        continue
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        embedding = model(image).squeeze().numpy()

    embeddings.append(embedding)
    dates.append(img_date)

# Save BOTH embeddings + dates together

np.savez(
    OUTPUT_PATH,
    embeddings=np.array(embeddings),
    dates=np.array(dates, dtype="datetime64[D]")
)

print(f"✅ Saved {len(embeddings)} embeddings with dates → {OUTPUT_PATH}")
