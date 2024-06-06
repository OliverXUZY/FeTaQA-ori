import json
import time 
from pprint import pprint
import pdb
from pdb import set_trace as pds

import sys
sys.path.insert(0, "/home/ubuntu/projects/FeTaQA-ori")

import os

import imgkit

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path, indent = 4):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = indent)

# Function to load JSON data from a file line by line
def load_json_lines(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data

# Function to save a list of JSON objects to a file, each JSON object on a new line
def save_json_lines(data, file_path):
    with open(file_path, 'w') as file:
        for json_obj in data:
            json_line = json.dumps(json_obj)
            file.write(json_line + '\n')

def ensure_path(path, early_exit = False):
    if os.path.exists(path):
        if early_exit:
            if input('{:s} exists, continue? ([y]/n): '.format(path)) == 'n':
                sys.exit(0)
    else:
        os.makedirs(path)

NUM_TABLES = 500
TOTTO_PATH = "./data/totto_source"
HTML_PATH = "./data/html"

def generate_html():
    ensure_path(HTML_PATH)
    for table_id in range(NUM_TABLES):
        totoo_source = load_json(f"{TOTTO_PATH}/dev_json/example-{table_id}.json")
        html_content = totoo_source['table_html']
        filename = f'{HTML_PATH}/dev_{table_id}.html'
        # Write the HTML content to the file
        with open(filename, "w") as file:
            file.write(html_content)



JPG_PATH = "./data/jpg"
def html2jpg():
    ensure_path(JPG_PATH)
    for table_id in range(NUM_TABLES):
        filename = f'{HTML_PATH}/dev_{table_id}.html'
        # pds()
        imgkit.from_file(filename, f'{JPG_PATH}/dev_{table_id}.jpg')





def main():

    #### generate html to "./data/html"
    generate_html()

    ### html to jpg to "./data/jpg"
    # html2jpg()




if __name__ == "__main__":
    main()