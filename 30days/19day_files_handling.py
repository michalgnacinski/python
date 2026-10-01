import os
import json
import csv
import xml.etree.cElementTree as ET
#Read
f = open('./assets/day19_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

#Readline
f1 = open('./assets/day19_example.txt')
lines = f1.readlines()
print(type(lines))
print(lines)
f1.close()

#Splitlines
f2 = open('./assets/day19_example.txt')
lines_split = f2.read().splitlines()
print(type(lines_split))
print(lines_split)
f2.close()

with open('./assets/day19_example.txt') as f3:
    lines_split2 = f3.read().splitlines()
    print(type(lines_split2))
    print(lines_split2)

#Appen and Write file
with open('./assets/day19_example.txt', 'a') as f4:
    f4.write('This text is added at the end')

with open('./assets/day19_example2.txt', 'w') as f5:
    f5.write('This text is added at the end of new file')

#Deleting files
if os.path.exists('./assets/day19_example2.txt'):
    os.remove('./assets/day19_example2.txt')
else:
    print('The file doesnt exist')

#JSON -> Dictionary
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

#Dictionary -> JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person_to_json = json.dumps(person, indent=4)
print(type(person_to_json))
print(person_to_json)

#Saving as JSON file
with open('./assets/json_example.json', 'w', encoding='utf-8') as f5:
    json.dump(person, f5, ensure_ascii=False, indent=4)

#CSV files - Coma Separated Values
with open('./assets/csv_example.csv') as f6:
    csv_reader = csv.reader(f6, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teacher. He lives in {row[0]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines: {line_count}')

#XML files
tree = ET.parse('./assets/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

#Exercise 1
with open('./assets/melina_trump_speech.txt', 'r') as ex1:
    reader = ex1.read()
    lines = ex1.readlines()
    lines_count = len(lines)
    words = reader.split()
    count_words = len(words)
    
print(f'Lines count: {line_count}, words count: {count_words}')

#Exercise 2
def most_spoken_lanugages(filename='./assets/countries_data.json', counter):
    with open(filename, 'r', encoding='utf-8') as kraje:
        countries = json.load(kraje)
        for kraj in range(counter):
            
print(most_spoken_lanugages())