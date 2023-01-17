# Script to affect (add, remove, change) tags in Obsidian files
# ToDo
# 2022-01-16
# - Recursive into directories instead of ignoring them
# - Function that takes the content, the string to change, the change to make, add/remove/change

import os

input_dir = '/Users/chrisbeaumont/chris.beaumont@gmail.com - Google Drive/My Drive/Obsidian/BULLET JOURNAL 2023/04 - PEOPLE/STATESPACE/ENGINEERING'
files = os.listdir(input_dir)

for file in files:
    file_path = f'{input_dir}/{file}'

    if file_path.endswith('.md'):
        print(file_path)

        # Get the file's contents
        f = open(file_path, 'r')
        content = f.read()
        f.close()
        
        # Do what you want to do to the tags
        content = content.replace("#Collection", '')
        print(content)
        
        # Overwrite the original file with the ammended content
        f = open(file_path, 'w')
        f.write(content)
        f.close()
