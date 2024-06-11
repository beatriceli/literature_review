import bibtexparser
import os 

# go into the literature folder and parse the bibtex file
os.chdir("literature")
# open the bibtex file
library = bibtexparser.parse_file('acm_2021-07-01_2024-05-31.bib')

print(f"Parsed {len(library.blocks)} blocks")
print(f"Found {len(library.entries)} entries")
# print first 5 entries
for i in range(2):
    # print(library.entries[i])
    print(library.entries[i].key)
    print(library.entries[i].entry_type)
    print(library.entries[i].fields)
    print(library.entries[i].fields_dict)