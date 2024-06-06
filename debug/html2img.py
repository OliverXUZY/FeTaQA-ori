import json
import time 
from pprint import pprint
import pdb

# h

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


def main():

    # totoo_source = load_json("./data/totto_source/dev_json/example-2274.json")
    # html_content = totoo_source['table_html']
    # filename = 'test.html'

    # # Write the HTML content to the file
    # with open(filename, "w") as file:
    #     file.write(html_content)

    imgkit.from_file('test.html', 'out.jpg')



    pdb.set_trace()


if __name__ == "__main__":
    main()