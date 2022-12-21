import os

def get_key_for_filename(filename):
    return filename.split('.')[0]

KEYS = [get_key_for_filename(fname) for fname in os.listdir('lines')]