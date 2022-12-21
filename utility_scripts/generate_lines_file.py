import json

root_file_path = 'workbench'

file_specs = [
    ('god', 'lines/hal_9000.txt'),
    ('car_manual', 'lines/claw_arm.txt'),
    ('bezos', 'lines/bezos_hologram.txt'),
    ('fenway_park_yelp_reviews', 'lines/boston_dynamics.txt'),
    ('final_boss', 'lines/final_boss.txt'),
    ('scouts_betrayal', 'lines/scouts_betrayal.txt'),
]

def list_item_for_keywords(keyword):
    return f"'{keyword}'"

prefix = """init python:
    LINES = """

TAGS = ['B', 'Q', 'R']

def append_to_entry(d, k, v):
    if not k in d:
        d[k] = []
    d[k].append(v)


lines = []

for name, path in file_specs:
    print(name, path)
    with open(path) as f:
        file_lines = [line for line in f.readlines()]
    
    for line in file_lines:
        text, love_level, tag = [elem.strip() for elem in line.split('\t')]
        if love_level == '':
            love_level = '3'
        if tag == '':
            tag = 'R'
        lines.append({'corpus': name, 'text': text, 'love_level': int(love_level), 'tag': tag})

with open('lines.rpy', 'w') as f:
    f.write(prefix + json.dumps(lines)+'\n')