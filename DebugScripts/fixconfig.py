# This script is used to split the dataset into train 
# and validation sets and reorganize the files into the correct folders.

import os
import shutil
import random

# Set paths
base_dir = '/Users/nathandeanon/Documents/CVProject/data'
images_dir = os.path.join(base_dir, 'images')
labels_dir = os.path.join(base_dir, 'labels')

# Output folders
train_img_dir = os.path.join(images_dir, 'train')
val_img_dir = os.path.join(images_dir, 'val')
train_lbl_dir = os.path.join(labels_dir, 'train')
val_lbl_dir = os.path.join(labels_dir, 'val')

# Make sure the output folders exist
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(train_lbl_dir, exist_ok=True)
os.makedirs(val_lbl_dir, exist_ok=True)

# Get all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]

# Shuffle and split
random.shuffle(image_files)
split_idx = int(len(image_files) * 0.8)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

def move_files(file_list, img_dst, lbl_dst):
    for img_file in file_list:
        # Move image
        src_img = os.path.join(images_dir, img_file)
        dst_img = os.path.join(img_dst, img_file)
        shutil.move(src_img, dst_img)

        # Move label with same base name
        label_file = os.path.splitext(img_file)[0] + '.txt'
        src_lbl = os.path.join(labels_dir, label_file)
        dst_lbl = os.path.join(lbl_dst, label_file)

        if os.path.exists(src_lbl):
            shutil.move(src_lbl, dst_lbl)
        else:
            print(f"⚠️ Warning: No label found for {img_file}")

# Move train and val sets
move_files(train_files, train_img_dir, train_lbl_dir)
move_files(val_files, val_img_dir, val_lbl_dir)

print("✅ Dataset split into train/val and reorganized successfully!")