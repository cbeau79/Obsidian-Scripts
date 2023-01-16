# Script that creates MD files for each week of the year for my Bullet Journal method
# 2023-01-15 - added the ability to include content for each file
#
# 
import os
from datetime import date

index = 6
week = 3
year = 2023
destination_dir = '/Users/chrisbeaumont/chris.beaumont@gmail.com - Google Drive/My Drive/Obsidian/BULLET JOURNAL 2023/01 - LOGS'

# Decided not to write the template to each file because I will probably want to change it as we go through the year and I can easily import it into each file as I begin to use it. Creating the structure is primarily a way of allowing me to easily throw work into the future.
# But here's the code for it anyway ...
'''
template_file = '/Users/chrisbeaumont/chris.beaumont@gmail.com - Google Drive/My Drive/Obsidian/BULLET JOURNAL 2023/99 - SYSTEM FILES/TEMPLATES/WEEK LOG TEMPLATE.md'

f = open(template_file, 'r')
contents = f.read()
f.close
'''

structure = {
    '8': '08 FEBRUARY.md',
    '14': '14 MARCH.md',
    '19': '19 Q2.md',
    '20': '20 APRIL.md',
    '25': '25 MAY.md',
    '31': '31 JUNE.md',
    '36': '36 Q3.md',
    '37': '37 JULY.md',
    '42': '42 AUGUST.md',
    '42': '42 AUGUST.md',
    '48': '48 SEPTEMBER.md',
    '53': '53 Q4.md',
    '54': '54 OCTOBER.md',
    '59': '59 NOVEMBER.md',
    '65': '65 NOVEMBER.md'
}

while True:
    # print(f'Index: {index}')
    if str(index) in structure.keys():
        filename = structure[str(index)]
    else:
        if week == 53:
            break
        
        if week < 10:
            monday_str = f"{year}-W0{week}-1"
            sunday_str = f"{year}-W0{week}-7"
        else:
            monday_str = f"{year}-W{week}-1"
            sunday_str = f"{year}-W{week}-7"
            
        monday = date.fromisoformat(monday_str)
        sunday = date.fromisoformat(sunday_str)

        if (monday.strftime("%b") == sunday.strftime("%b")):
            dst_dates = f"{monday.strftime('%b').upper()} {monday.strftime('%d')} TO {sunday.strftime('%d')}"
        else:
            dst_dates = f"{monday.strftime('%b').upper()} {monday.strftime('%d')} TO {sunday.strftime('%b').upper()} {sunday.strftime('%d')}"
        
        if week < 10:
            filename = f'WEEK 0{week} - {dst_dates}.md'
        else:
            filename = f'WEEK {week} - {dst_dates}.md'

        if index < 10:
            filename = f'0{index} {filename}'
        else:
            filename = f'{index} {filename}'
        
        week += 1

    file_path = f'{destination_dir}/{filename}'

    print(file_path)

    f = open(file_path, 'w+')
    f.write("You're doing your best. Be kind and keep going.")
    f.close

    index +=1
