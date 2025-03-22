# Description: This script renames all .jpeg files in the specified directories to .jpg files.
# I did this cause MacOS uses .jpeg as the default extension for images, but YOLOv5 expects .jpg files.


import os

def rename_jpegs_to_jpg(folder):
    renamed = 0
    for filename in os.listdir(folder):
        if filename.lower().endswith('.jpeg'):
            old_path = os.path.join(folder, filename)
            new_filename = filename[:-5] + '.jpg'
            new_path = os.path.join(folder, new_filename)
            os.rename(old_path, new_path)
            renamed += 1
    return renamed

image_dirs = [
    '/Users/nathandeanon/Documents/CVProject/data/images/train',
    '/Users/nathandeanon/Documents/CVProject/data/images/val'
]

total = 0
for dir_path in image_dirs:
    count = rename_jpegs_to_jpg(dir_path)
    print(f"✅ Renamed {count} .jpeg files in {dir_path}")
    total += count

print(f"\n🎉 Done! Renamed {total} images total.")