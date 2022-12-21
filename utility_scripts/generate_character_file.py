import tfidf

root_file_path = 'workbench'

file_specs = [
    ('god', 'workbench/bible_god_delusion.txt'),
    ('car_manual', 'workbench/car-manual.txt'),
    ('bezos', 'workbench/bezos.txt'),
    ('fenway_park_yelp_reviews', 'workbench/fenway_park_yelp.txt'),
    ('final_boss', 'workbench/taylor_bodybuilding_pancakes.txt'),
    ('scouts_betrayal', 'workbench/scouts_betrayal.txt')
]

def list_item_for_keywords(keyword):
    return f"'{keyword}'"

file_text = """init python:
    KEYWORDS = {
<PAIRS>
    }
"""

import string

def remove_punctuation(text):
    exclude = set(string.punctuation)
    return ''.join(ch for ch in text if ch not in exclude)

def has_numbers(text):
    for c in text:
        if c.isdigit():
            return True
    return False

entries = []
for name, path in file_specs:
    print(name, path)
    keywords = tfidf.get_keywords_from_file_and_directory(path, root_file_path)
    
    ## Filter keywords
    keywords = [remove_punctuation(k) for k in keywords]
    keywords = [k for k in keywords if not has_numbers(k)]
    keywords = [k for k in keywords if len(k) > 1]

    keyword_items = [list_item_for_keywords(k) for k in keywords]
    normalized_name = name.replace(' ','_').lower()
    entry_text = f"        '{normalized_name}': [{', '.join(keyword_items)}],"
    entries.append(entry_text)
all_entries_text = '\n'.join(entries)
file_text = file_text.replace('<PAIRS>', all_entries_text)

with open('keywords.rpy', 'w') as f:
    f.write(file_text)