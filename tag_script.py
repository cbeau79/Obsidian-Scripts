# Script to affect (add, remove, change) tags in Obsidian files
import os

input_dir = '/Users/chrisbeaumont/chris.beaumont@gmail.com - Google Drive/My Drive/Obsidian/BULLET JOURNAL 2023/04 - PEOPLE/STATESPACE/ENGINEERING'
files = os.listdir(input_dir)

for file in files:
    file_path = f'{input_dir}/{file}'

    if file_path.endswith('.md'):
        print(file_path)
        f = open(file_path, 'r')
        content = f.read()
        content = content.replace("#Collection", '')
        print(content)
        f.close()
        f = open(file_path, 'w')
        f.write(content)
        f.close()
