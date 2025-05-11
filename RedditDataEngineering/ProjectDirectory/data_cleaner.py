import csv
from datetime import datetime

input_file = r'data/reddit_posts.csv'      # Raw CSV file from extraction
output_file = r'data/reddit_posts_cleaned.csv'  # Cleaned output file

# Define the correct header
header = ['id', 'title', 'score', 'created_datetime', 'created_date', 'title_word_count']

def unix_to_datetime(unix_ts):
    try:
        return datetime.fromtimestamp(float(unix_ts)).strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return ''

def unix_to_date(unix_ts):
    try:
        return datetime.utcfromtimestamp(float(unix_ts)).strftime('%Y-%m-%d')
    except Exception:
        return ''

def word_count(text):
    return len(text.split()) if text else 0

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(header)
    for row in reader:
        id_ = row.get('id', '').strip()
        title = row.get('title', '').strip()
        score = row.get('score', '').strip()
        created = row.get('created', '').strip()
        created_datetime = unix_to_datetime(created)
        created_date = unix_to_date(created)
        title_word_count = word_count(title)
        writer.writerow([id_, title, score, created_datetime, created_date, title_word_count])

print(f"Cleaned CSV saved as {output_file}")