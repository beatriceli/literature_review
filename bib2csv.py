import re
import csv
import os

def parse_bib_entry(entry):
    fields = dict(re.findall(r'(\w+)\s*=\s*\{((?:[^{}]|(?:\{(?:[^{}]|(?:\{[^{}]*\}))*\}))*?)\}', entry))
    
    return {
        'title': fields.get('title', ''),
        'abstract': fields.get('abstract', ''),
        'author': fields.get('author', ''),
        'SourceTitle': fields.get('journal', fields.get('booktitle', '')), # journal or booktitle
        'year': fields.get('year', ''),
        'keywords': fields.get('keywords', ''),
        'doi': fields.get('doi', '')
    }

def export_to_csv(bib_file, output_file):
    with open(bib_file, 'r', encoding='utf-8') as f:
        bib_content = f.read()

    # Split bib file into entries, each entry starts with @
    entries = re.split(r'@(\w+)\s*{', bib_content)
    # Pair entry types with their corresponding entries
    entries = [(entries[i], entries[i+1]) for i in range(1, len(entries), 2)]
    print(f'Found {len(entries)} entries')

    data = [parse_bib_entry(entry) for entry_type, entry in entries]

    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Abstract', 'Author', 'SourceTitle', 'Publication Year', 'Keywords','DOI'])
        for entry in data:
            writer.writerow([
                entry['title'],
                entry['abstract'],
                entry['author'],
                entry['SourceTitle'],
                entry['year'],
                entry['keywords'],
                entry['doi']
            ])


if __name__ == '__main__':
    # bib file is in literature directory
    bib_file = 'literature/acm_2021-07-01_2024-05-31.bib'
    # the outfile should be generated based off of the start and end date in the filename
    # e.g. lit_acm_2021-07-01_2024-05-31.csv
    # get the start and end date from the filename
    start_date = bib_file.split('_')[1]
    end_date = bib_file.split('_')[2].split('.')[0]
    output_file = f'lit_acm_{start_date}_{end_date}.csv'

    # check if literature directory exists
    if not os.path.exists("literature"):
            os.makedirs("literature")
    filename = os.path.join("literature", output_file)

    export_to_csv(bib_file, filename)