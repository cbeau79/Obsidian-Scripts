import os
import csv
import re
from datetime import date

# I want this script to read each line of the Journal CSV file and then write it as an MD file in an Obsidian vault using the date as the filename
# It will need to clean each entry and remove empty entries, and grab attached media files and store them in an appropriate place

# VARIABLES
vault_path = 'DayOneVault/'
media_path = f'{vault_path}Media'
journal = 'journal_test.csv'

# DICT OF TERMS -> HASHTAGS
terms = {
	"dad": "Family",
	"father": "Family",
	"mum": "Family",
	"mother": "Family",
	"patrick": "Family",
	"pat": "Family",
	"brother": "Family",
	"natasha": "Relationships",
	"alicia": "Relationships",
	"ali": "Relationships",
	"Rosalie": "Marriage",
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
	"photo": "Photography",
	"photos": "Photography",
	"exercise": "Health",
	"dream": "Dream",
	"therapy": "Therapy",

}

# OPEN CSV AND BEGIN BEGIN PROCESSING ITS CONTENTS
with open(journal) as file_obj:

	reader_obj = csv.DictReader(file_obj)
	
	for row in reader_obj:

			# Strip HTML tags
			text = row['text']
			clean = re.compile('<.*?>')
			text = re.sub(clean, '', text)
			
			# Replace '• ' with '- '
			# text.replace("â€¢", "- ") # <<< it's not picking this up for some reason
			
			# CHECK text FOR POTENTIAL HASHTAGS
			hashtags = []
			for k, v in terms.items():
				if k in text.lower():
					hashtags.append(v)

			hashtags = list(dict.fromkeys(hashtags))	
			print(f'This entry has the following hashtags {hashtags}')
#			del hashtags

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
