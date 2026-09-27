"""
Module 2 — Activity: File Sorting with os and shutil
Student: Ethan Miguel P. Patio
Date: September 26, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built a simple file sorter code that automatically organizes messy folders by using their extensions

============================================
KEY VOCABULARY
============================================
- os module: a built-in python library, it provides a functions to use with the os
- shutil module: also a build-in python library, useful for copying, moving, renaming, and deleting files or folder
- file path: location of your file stored within a computer (ex. D:\ETHAN\WALLPAPER\image.png)
- directory: used to organize and store files/folders
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

folder_path = "D:\ETHAN\WALLPAPER"

for file in os.listdir(folder_path):
    name, ext = os.path.splitext(file)
    ext = ext.replace(".", "").lower()

    if ext:
        target_folder = folder_path + "/" + ext
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(folder_path + "/" + file, target_folder + "/" + file)

print("Files are sorted into folders")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
The mistake I made is forgetting to use the shutil when trying to move the file 

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
