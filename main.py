# INDIAN_SCRAPE = [
#     "https://api.apify.com/v2/datasets/KyUbmFRfiKjNSTLDa/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/ME0Uveb3BfZf7Ty6H/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/IUoRgvcV2D2daazhe/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/1PKO5LKR95TiDuxmT/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/t6SHkdDnLWbYBhEYI/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/X32yrliWgMyvSwjXG/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/9DVn4CTSas0eW1unN/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/jyrXAvMdcEPcd6fOT/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/VjsLDyNv3sdf5fotp/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/pNuG6dviC4KhvFfSC/items?format=json&clean=true"
#     ]
#
# US_SCRAPE = [
#     "https://api.apify.com/v2/datasets/A1GJqy4j7ZmI6o5AM/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/s6fR2FzPKKtFsHSFC/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/j16RXgPbu4sTaaRNJ/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/0KaZEqt69eaXhkV2P/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/XcONIaTDD7GqdUB0K/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/KFmw2agDh3IJq31WP/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/2jTvqXzXIoBiR2hlA/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/aNsxHNK02marUAcZN/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/tNnzNvNshD8bQGq7n/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/YeSNudhitpzNdU2y6/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/haGvn7ipDPRVIeVqp/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/Lt9Zqx8Hg2aq3uata/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/A6D62Nc1PboCRKGJM/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/EOOxAHgh2hJK1eZqo/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/GJ8agjsxToupa7aoY/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/RL9FB7NxsuyJKIIFX/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/6vs6F6oewKaDbH0D2/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/CI46ONy4KtKcdupeH/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/a4dK6j8CsTG86STkU/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/vgqeDvOtxHOJrFcKR/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/jd7p0pdSvLpEeWA2a/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/NUlVNToFQoNCizcMH/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/mBQA1KTpSL7O3ho4F/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/Lo54NDG9mVpn7k7g6/items?format=json&clean=true",
#     "https://api.apify.com/v2/datasets/5Yo4fm1Z9a2uO4Hlo/items?format=json&clean=true"
# ] # 2001 IMAGES
#
# import os
# import requests
# from datetime import datetime
# import pandas as pd
#
# OUTPUT_DIR = "data/indian_images"
# os.makedirs(OUTPUT_DIR, exist_ok=True)
#
# def download_image(url, filename):
#     try:
#         r = requests.get(url, stream=True, timeout=10)
#         r.raise_for_status()
#
#         with open(filename, "wb") as f:
#             for chunk in r.iter_content(8192):
#                 f.write(chunk)
#
#         return True
#     except Exception as e:
#         print(f"❌ Failed: {url}")
#         return False
#
# i = 1
#
# for link in INDIAN_SCRAPE:
#     json_file = requests.get(link).json()
#     for post in json_file:
#         try:
#             image_url = post["displayUrl"]
#             date = post['timestamp'].split('T')[0]
#             filename = f"{OUTPUT_DIR}/{date}_{i}.jpg"
#         except KeyError:
#             continue
#
#         if os.path.exists(filename):
#             continue  # skip already downloaded images
#
#         download_image(image_url, filename)
#         i += 1


import os
from PIL import Image
import imagehash

def remove_duplicate_images(
    image_dir,
    hash_size=16,
    threshold=5
):
    hashes = {}
    removed = 0

    for file in os.listdir(image_dir):
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        path = os.path.join(image_dir, file)

        try:
            # IMPORTANT: context manager closes the file
            with Image.open(path) as img:
                img = img.convert("RGB")
                h = imagehash.phash(img, hash_size=hash_size)

            duplicate = False
            for existing_hash in hashes:
                if h - existing_hash <= threshold:
                    duplicate = True
                    break

            if duplicate:
                os.remove(path)
                removed += 1
            else:
                hashes[h] = path

        except Exception:
            try:
                os.remove(path)
                removed += 1
            except PermissionError:
                print(f"⚠️ Skipped locked file: {file}")

    print(f"Removed {removed} duplicate/corrupt images")

# Run
remove_duplicate_images("data/global_images")


