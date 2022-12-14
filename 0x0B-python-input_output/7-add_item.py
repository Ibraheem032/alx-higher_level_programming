#!/usr/bin/python3
"""Adds all argument to a list and save it as a JSON file.
"""
import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
my_list = []
for arg in sys.argv[1:]:
    my_list.append(arg)
x = load_from_json_file('add_item.json')
my_list = x + my_list
save_to_json_file(my_list, 'add_item.json')
