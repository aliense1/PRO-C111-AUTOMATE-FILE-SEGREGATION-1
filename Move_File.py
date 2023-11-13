import os
import shutil

from_dir = "C:/Users/HP/Downloads"

to_dir = "C:/Users/HP/OneDrive/Desktop/Document_files"

list_of_files = os.listdir(from_dir)

for i in list_of_files:
    root,ext = os.path.splitext(i)
    print(root+"   "+ext)
