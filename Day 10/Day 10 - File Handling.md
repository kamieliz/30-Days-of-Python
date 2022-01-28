# Day 10 - File Handling

# Table of Contents

1. [File Handling](craftdocs://open?blockId=2F1A4957-9905-4621-95BE-7556DBC1079D&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [Opening files for reading](craftdocs://open?blockId=364D634A-06A6-4C26-9FBF-67128C2060F7&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
2. [File Types](craftdocs://open?blockId=694C252F-75A5-466C-9911-12D5588A0B68&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   1. [JSON](craftdocs://open?blockId=D248499A-E258-418F-8AFB-0AEADC3CBD82&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   2. [CSV](craftdocs://open?blockId=80BC6A23-3001-4E30-A21A-F3D76C38792E&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   3. [XLSX](craftdocs://open?blockId=759A5A4E-07BC-4380-8A72-2E18FE8718F0&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)
   4. [XML](craftdocs://open?blockId=42C6622A-0B9F-4467-A55F-D9C2B186B67F&spaceId=d367a179-adcb-7ce8-0b02-ba52d2a7c917)

# File Handling

- usually data is stored in different file formats like .txt, .json, .xml, .csv, etc
- file handling is an important part of programming bc it allows you to create, read, update and delete files.
- use open() built in function to handle data

```other
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
```

   - r - read - default value, opens a file for reading, returns an error if it doesnt exist
   - a - append - opens a file for appending, creates a file if it doesnt exist
   - w - write - opens a file for writing, creates a file if it doesn’t exist
   - “x” - create - creates specified file, returns error if file exists
   - t - text - default value - text mode
   - b - binary - binary mode for images

## Opening files for reading

- the default mode of open is reading, so you do not have to specify r or rt
- opened files have different reading methods:
   - read() - reads the whole text as string. can limit the number characters read by passing an int value to method
      - `txt = file.read()`
   - readline() - reads only the first line
      - `txt = file.readline()`
   - readlines() - read all the text line by line and return a list of lines
      - `txt = file.readlines()`
   - another way to get all the lines as a list is using splitlines()
      - `txt = file.read().splitlines()`
- when you open a file, make sure you close it either with close() or by opening files using with
   - `file.close()`

```other
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

- can use write() method to append or write new text

```other
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

- remove() removes a file but requires the os module
   - if file doesn’t exist it will raise an error

```other
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

# File Types

## JSON

- stands for JavaScript Object Notation
- very similar to a python dictionary
- to change a json file to a dictionary:
   - import json module
   - use loads method

```other
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

- to change a dictionary into json use the dumps method from json module
- can also save data as a json file:
   - use the json.dump() method
   - output file
   - ensure ascii
   - indent

```other
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

## CSV

- comma separated values
- simple file format used to store tabular data, such as a spreadsheet or database
- very common data format in data science
- use csv module when working with these files

```other
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

## XLSX

- to read excel fileds, need to install xlrd package
   - `pip install xlrd`

```other
import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

## XML

- structured data format which looks like HTML
- tags are not predefined
- the first line is an XML declaration
- import [xml.etree.ElementTree](https://docs.python.org/2/library/xml.etree.elementtree.html)

```other
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```

