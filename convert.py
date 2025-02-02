import os
import bson
import json
path_to_file = input()

try:
    with open(path_to_file, 'rb') as f:
        data = bson.decode(f.read())
except FileNotFoundError:
    print('dont mispell!')
    os.system('shutdown -s')
    exit()

with open('output_json_file.json', 'w') as f:
    json.dump(data, f, indent=4)