# Description: This script checks if the image and label pairs in the training and validation datasets match correctly.
# It prints any missing pairs or mismatches found.

import os

# Define your paths
image_train_dir = "/Users/nathandeanon/Documents/CVProject/data/images/train"
label_train_dir = "/Users/nathandeanon/Documents/CVProject/data/labels/train"
image_val_dir = "/Users/nathandeanon/Documents/CVProject/data/images/val"
label_val_dir = "/Users/nathandeanon/Documents/CVProject/data/labels/val"

# Function to get file names without extensions
def get_base_filenames(directory, extensions):
    return {os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(extensions)}

# Get train and val image/label base names
train_images = get_base_filenames(image_train_dir, (".jpg", ".jpeg", ".png"))
train_labels = get_base_filenames(label_train_dir, (".txt",))
val_images = get_base_filenames(image_val_dir, (".jpg", ".jpeg", ".png"))
val_labels = get_base_filenames(label_val_dir, (".txt",))

# Find mismatches
missing_train_labels = train_images - train_labels
missing_train_images = train_labels - train_images
missing_val_labels = val_images - val_labels
missing_val_images = val_labels - val_images

# Print results
print("🔍 Checking dataset consistency...\n")

if missing_train_labels:
    print(f"⚠️ Training images missing labels ({len(missing_train_labels)}):")
    print("\n".join(missing_train_labels))

if missing_train_images:
    print(f"⚠️ Training labels missing images ({len(missing_train_images)}):")
    print("\n".join(missing_train_images))

if missing_val_labels:
    print(f"⚠️ Validation images missing labels ({len(missing_val_labels)}):")
    print("\n".join(missing_val_labels))

if missing_val_images:
    print(f"⚠️ Validation labels missing images ({len(missing_val_images)}):")
    print("\n".join(missing_val_images))

if not (missing_train_labels or missing_train_images or missing_val_labels or missing_val_images):
    print("✅ All images and labels match correctly!")