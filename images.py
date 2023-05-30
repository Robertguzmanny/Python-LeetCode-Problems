import os
import shutil

download_folder = os.path.expanduser("~/Downloads")
images_folder = os.path.expanduser("~/Downloads/images")

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

for file_name in os.listdir(download_folder):
    if file_name.endswith(".PNG") or file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        file_path = os.path.join(download_folder, file_name)
        shutil.move(file_path, images_folder)
