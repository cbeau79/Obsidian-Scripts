# NOTION TO OBSIDIAN
# Specifically, my 'Notes' database from Feb 2021 to Oct 2021
# Each file has the following header:
'''
# Aim Lab Tone & Community Guidelines

Created: June 13, 2022 11:51 AM
Date: August 2, 2022
Last updated: August 1, 2022 9:44 PM
Mood: Good
Status: Active
Type: Doc
'''
# Ideal solution - open each file, get the 'Date', add that content to it's appropriate 'Week' note, in correct Date order. That's pretty tricky.
# Jank solution - open each file, get the 'Date', rename the file with the Date at the start, that's it

import os
from datetime import datetime
from datetime import date

dir_path = '/Users/chrisbeaumont/Desktop/PERSONAL/Note Taking Purgatory/Notes Exports/Chris\' Notion - Notes and Weeks 2202 to 2210/Notes'
output_path = './temp_output/'
files = os.listdir(dir_path)
file_list = []

for file in files:
    file_path = f'{dir_path}/{file}'

    # Process this file
    if os.path.isfile(file_path) and os.path.getsize(file_path) != 0 and file.startswith('.') != True:
        print(f'Opening file: {file}')
        f = open(file_path, 'r')
        count = 0

        raw_date = ''  
        week = ''
        iso_date = ''
        d = ''
        mood = ''
        content = ''
        collect_content = False
        title = ''

        while True:
            line = f.readline()

            if count == 0:
                title = line
            
            count += 1

            # Get the date 
            if line.startswith('Date: '):
                raw_date = line.partition('Date: ')[2]
                readable_date = raw_date
                raw_date = raw_date.replace(',', '')
                raw_date = raw_date.replace('\n', '')
                # print(raw_date)

                # Break date into chunks
                chunks = raw_date.split(' ')
                month = int(datetime.strptime(chunks[0], '%B').month)
                day = int(chunks[1])
                year = int(chunks[2])
                if month < 10:
                    month = f'0{month}'
                if day < 10:
                    day = f'0{day}'

                iso_date = f'{year}-{month}-{day}'

                # create a date object
                d = date.fromisoformat(iso_date)

                # figure out what the week number is
                week = d.isocalendar().week

                #print(iso_date)
                #print(week)

            # If this is the last line of the meta data ('Type') set a boolean
            if line.startswith('Mood: '):
                mood = line.partition('Mood: ')[2]

            if collect_content:
                content += line

            # If this is the last line of the meta data ('Type') set a boolean
            if line.startswith('Type: '):
                collect_content = True

            if not line:
                break

        file_list.append(
            {
                'file_path': file_path,
                'title': title.strip(),
                'date': iso_date,
                'readable_date': readable_date.strip(),
                'week': week,
                'content': content,
                'mood': mood.strip(),
            }
        )

        #print(len(file_list))
        #print('\n\n')

# Ok, build the weeks - gotta do it like, build week 14: build monday, build tuesday, build wednesday etc

week_number = 14 

while week_number < 47:
    print(f'Building Week {week_number}')

    week_output = f'# WEEK {week_number}\n\n'

    days_of_the_week = {
        "MONDAY": datetime.fromisoformat(f'2022-W{week_number}-1'),
        "TUESDAY": datetime.fromisoformat(f'2022-W{week_number}-2'),
        "WEDNESDAY": datetime.fromisoformat(f'2022-W{week_number}-3'),
        "THURSDAY": datetime.fromisoformat(f'2022-W{week_number}-4'),
        "FRIDAY": datetime.fromisoformat(f'2022-W{week_number}-5'),
        "SATURDAY": datetime.fromisoformat(f'2022-W{week_number}-6'),
        "SUNDAY": datetime.fromisoformat(f'2022-W{week_number}-7')
    }

    for day, date_obj in days_of_the_week.items():
        print(f'Building {day}')

        day_output = f'# {day}\n'
        day_output += date_obj.strftime("%Y-%m-%d")
        day_output += '\n\n'

        for entry in file_list:
            if entry['week'] == week_number:
                d = datetime.fromisoformat(entry['date'])
                day_of_the_week = d.strftime('%A')
                # print(f'{entry["date"]} is a {day_of_the_week}')

                if day_of_the_week.upper() == day:
                    day_output += f"#{entry['title']}"
                    day_output += entry['content']
                    day_output += '\n\n'
        
        week_output += day_output

    if (days_of_the_week['MONDAY'].strftime("%b") == days_of_the_week['SUNDAY'].strftime("%b")):
        output_file_path = f"{output_path}WEEK 22-{week_number} - {days_of_the_week['MONDAY'].strftime('%b').upper()} {days_of_the_week['MONDAY'].strftime('%d')} to {days_of_the_week['SUNDAY'].strftime('%d')}.md"
    else:
        output_file_path = f"{output_path}WEEK 22-{week_number} - {days_of_the_week['MONDAY'].strftime('%b').upper()} {days_of_the_week['MONDAY'].strftime('%d')} to {days_of_the_week['SUNDAY'].strftime('%b').upper()} {days_of_the_week['SUNDAY'].strftime('%d')}.md"

    f = open(output_file_path, 'w+')
    f.write(week_output)
    f.close()
    print(f"{output_file_path} has been written")

    week_number += 1







'''

for entry in file_list:

    filename = f"{entry['date']}{entry['title'].replace('#', '')}.md"
    print(filename)

    content = entry['title']
    content += '\n'
    content += f"**{entry['readable_date']}**"
    content += '\n'
    content += f"Week **{entry['week']}"
    content += '\n'
    content += f"**Mood: **{entry['mood']}"
    content += '\n'
    content += entry['content']

    # print(content)
    # print('\n\n---\n\n')

    output_file_path = f"{output_path}{filename.replace('/', '-').replace(':', '-')}"

    f = open(output_file_path, 'w+')
    f.write(content)
    print(f"{output_file_path} has been written")
    f.close()

        
'''