#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save them to a file.
"""
import sys
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

if len(sys.argv) > 1:
    new_list = sys.argv[1:]
else:
    new_list = []
try:
    my_list = load('add_item.json')
except FileNotFoundError:
    my_list = []
save(my_list + new_list, 'add_item.json')
