# Script that creates MD files for each week of the year for my Bullet Journal method
import os
from datetime import date

week = 14
year = 2022
destination_dir = '/Users/chrisbeaumont/Google Drive/My Drive/Obsidian/JOURNAL ARCHIVES/01 - Logs/2022'

while True:
    if week == 47:
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
        dst_dates = f"{monday.strftime('%b').upper()} {monday.strftime('%d')} to {sunday.strftime('%d')}"
    else:
        dst_dates = f"{monday.strftime('%b').upper()} {monday.strftime('%d')} to {sunday.strftime('%b').upper()} {sunday.strftime('%d')}"
    
    if week < 10:
        filename = f'WEEK 22-0{week} - {dst_dates}.md'
    else:
        filename = f'WEEK 22-{week} - {dst_dates}.md'

    file_path = f'{destination_dir}/{filename}'

    print(file_path)

    f = open(file_path, 'w+')
    f.write(f'# Week 22-{week}')
    f.close

    week += 1
