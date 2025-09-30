#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and then saves
the list to a file in JSON format.

- Uses save_to_json_file from 5-save_to_json_file.py
- Uses load_from_json_file from 6-load_from_json_file.py
- The list is saved in a file named add_item.json
- If the file does not exist, it will be created
"""

import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
