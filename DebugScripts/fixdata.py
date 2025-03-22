#Description: This script is used to fix the data in the dataset.
#It splits the dataset into train and validation sets and reorganizes the files into the correct folders.
#It also checks if the image and label pairs in the training and validation datasets match correctly.


import os
import random
import shutil

# Base directory
base_dir = "/Users/nathandeanon/Documents/CVProject/data"
image_dir = os.path.join(base_dir, "images")
label_dir = os.path.join(base_dir, "labels")

# Train/Val Paths
image_train_dir = os.path.join(image_dir, "train")
image_val_dir = os.path.join(image_dir, "val")
label_train_dir = os.path.join(label_dir, "train")
label_val_dir = os.path.join(label_dir, "val")

# Ensure output folders exist
for folder in [image_train_dir, image_val_dir, label_train_dir, label_val_dir]:
    os.makedirs(folder, exist_ok=True)

# Collect valid image-label pairs
valid_pairs = []
for split in ["train", "val"]:
    img_path = os.path.join(image_dir, split)
    lbl_path = os.path.join(label_dir, split)

    for filename in os.listdir(img_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            base = os.path.splitext(filename)[0]
            label_file = base + ".txt"
            label_path = os.path.join(lbl_path, label_file)

            # Debugging: Print each filename and whether its label exists
            print(f"Checking: {filename} → Label exists: {os.path.exists(label_path)}")

            if os.path.exists(label_path):
                valid_pairs.append((os.path.join(img_path, filename), os.path.join(lbl_path, label_file)))

# Print how many valid pairs we found
print(f"🔍 Found {len(valid_pairs)} valid image-label pairs.")

# If we found pairs, shuffle and split 80/20
if valid_pairs:
    random.shuffle(valid_pairs)
    split_idx = int(0.8 * len(valid_pairs))
    train_pairs = valid_pairs[:split_idx]
    val_pairs = valid_pairs[split_idx:]

    def move_pairs(pairs, img_dest, lbl_dest):
        for img_file, lbl_file in pairs:
            shutil.copy2(img_file, img_dest)
            shutil.copy2(lbl_file, lbl_dest)

    move_pairs(train_pairs, image_train_dir, label_train_dir)
    move_pairs(val_pairs, image_val_dir, label_val_dir)

    print(f"✅ Done! {len(train_pairs)} training pairs, {len(val_pairs)} validation pairs.")
else:
    print("❌ No valid image-label pairs found. Check filenames and paths!")