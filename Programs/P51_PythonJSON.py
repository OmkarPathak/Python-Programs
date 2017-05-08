# Author: OMKAR PATHAK
# This example shows how to use Python with JSON

import json

# For storing on json format
def storeJSON(fileName, data = {}):
    with open(fileName, 'w')  as fd:
        json.dump(data, fd, indent = 4, separators = (',', ': '))

# For loading data from a JSON file
def loadJSON(fileName):
    with open(fileName) as fd:
        data = json.load(fd)
        print(data)
    return data

if __name__ == '__main__':
    data = loadJSON('example.json')
    print(data['menu']['value'])        # File
    data['menu']['value'] = 'movie'
    storeJSON('example.json', data)
    print()
    loadJSON('example.json')
    print(data['menu']['value'])        # movie
