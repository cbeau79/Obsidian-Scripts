import os
import csv
import re
from datetime import date

# I want this script to read each line of the Journal CSV file and then write it as an MD file in an Obsidian vault using the date as the filename
# It will need to clean each entry and remove empty entries, and grab attached media files and store them in an appropriate place

# VARIABLES
vault_path = 'DayOneVault/'
media_path = f'{vault_path}Media'
journal = 'Journal.csv'

# DICT OF TERMS -> HASHTAGS
terms = {
	"dad": "Family",
	"father": "Family",
	"mum": "Family",
	"mother": "Family",
	"patrick": "Family",
	"pat": "Family",
	"brother": "Family",
	"natasha": ["Relationships", "Natasha"],
	"alicia": ["Relationships", "Alicia"],
	" ali ": ["Relationships", "Alicia"],
	"rosalie": ["Relationships", "Marriage", "Rosalie"],
	"ollie": "Oliver",
	"oliver": "Oliver",
	"parenting": ["Oliver", "Parenting"],
	"work": "Work",
	"money": "Finances",
	"investing": "Finances",
	"vanguard": "Finances",
	"finance": "Finances",
	"cbs": "Work",
	"cbsi": "Work",
	"gamespot": "Work",
	"statespace": "Work",
	"aim lab": "Work",
	"photography": "Photography",
	"exercise": "Health",
	"dream": "Dream",
	"therapy": "Therapy",
	"america": "America",
	"odpm1" : "ODPM",
	"mariya" : "Therapy",
	"self-acceptance" : "Therapy",
	"self-love" : "Therapy",
	"self-forgiveness" : "Therapy",
	"mastermind" : "ODPM",
	"marriage" : "Marriage"
}

# OPEN CSV AND BEGIN BEGIN PROCESSING ITS CONTENTS
with open(journal) as file_obj:

	reader_obj = csv.DictReader(file_obj)
	
	for row in reader_obj:

		# Break down row['date'] into useful chunks
		date_iso = row['date'][0:10]
		year = row['date'][0:4]
		month = row['date'][5:7]
		day = row['date'][8:10]
		time = row['date'][11:19].replace(':', '')
		d = date.fromisoformat(date_iso)
		day_of_the_week = d.strftime("%a")
		full_day_of_the_week = d.strftime("%A")
		full_month = d.strftime("%B")
		readable_date = f'{full_day_of_the_week}, {day} {full_month} {year}'

		print(f'\n\n------\n')
		print(f'{date_iso}B{time} Processing')
		print(f'{readable_date}')
		
		# Skip over entries that have no text and no media - they are empty
		if row['text'] == '' and row['mediaMD5s'] == '':
			print(row['uuid'],' has no useful data - skipping')

		else:
			hashtags = []

			# Build the full path for the entry
			entry_full_path = f'{vault_path}{year}/{date_iso} {day_of_the_week} {time}.md'
			print(f'Full Path: {entry_full_path}')
	
			# If the path doesn't exist, create it
			if not (os.path.exists(f'{vault_path}{year}')):
				os.makedirs(f'{vault_path}{year}')
				print(f'Directory created {vault_path}{year}')
	
			# Create the file for the entry
			f = open(entry_full_path, "w+")
			
			# Construct the entry
			entry = f'# {readable_date}\n'

			# If there are images, add them
			if row['mediaMD5s'] != '':
				hashtags.append('Photo');
				images = row['mediaMD5s'].split(", ")
				print(f'There\'s {len(images)} photo(s)')

				for image in images:
					image_url = f'![[{image}.jpeg]]'
					print(image_url)
					entry += image_url
					
				entry += "\n"
			
			# Strip HTML tags
			text = row['text']
			print(text)
			clean = re.compile('<.*?>')
			text = re.sub(clean, '', text)
			print('After HTML tags stripped\n', text)
			
			# Replace '• ' with '- '
			text = text.replace("• ", "- ")
			
			# CHECK text FOR POTENTIAL HASHTAGS, BUILD HASHTAGS LIST
			for k, v in terms.items():
				if k in text.lower():
					if isinstance(v, list):
						for tag in v:
							hashtags.append(tag)
					else:
						hashtags.append(v)

			# ADD THE text
			entry += text
			entry += "\n\n### Metadata\n"
			
			# CLEAN LOCATION DATA & ADD TO hashtags
			country = row['country']
			if country != '': 
				if country == 'London' or country == 'Greater London' or country == 'United Kingdom' or country == 'Cornwall' or country == 'East Sussex' or country == 'Essex' or country == 'Suffolk' or country == 'TR11':
					country = 'England'
				elif country == 'United States':
					country = 'America'
				
				hashtags.append(country.replace(" ", ""))
				country = ''
			
			area = row['administrativeArea']
			if area != '':
				if area == 'England' or area == 'United Kingdom':
					# DO NOTHING
					this_var = ''
				else:
					if area == 'CA':
						area = 'California'
					if area == 'Greater London':
						area = 'London'
					if area == 'OR':
						area = 'Oregon'
					if area == 'NY':
						area = 'New York'
					if area == 'HI':
						area = 'Hawaii'
					if area == 'Downtown' or area == 'South Los Angeles' or area == 'Los Angeles' or area == 'Los Angeles County':
						area = 'Los Angeles'
				
					if area == '':
						area = area
					
					hashtags.append(area.replace(" ", ""))
			
			# REMOVE DUPLICATES FROM HASHTAGS
			hashtags = list(dict.fromkeys(hashtags))
			
			if len(hashtags) > 0: print('These hashtags were found:')
			# ADD HASHTAGS
			for hashtag in hashtags:
				entry += f'#{hashtag} '
				print(hashtag)
			
			# WRITE THE FILE & CLOSE
			f.write(entry)
			f.close()
			
			print(f'{entry_full_path} has been written')
	
