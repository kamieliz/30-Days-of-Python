# write a function that counts number of lines and number of words in a text
def num_lines_words(file):
    opened_file = open(file, 'r')
    num_lines = 0
    num_words = 0
    result = []
    for line in opened_file:
        line = line.strip('\n')
        words = line.split()
        num_lines += 1
        num_words += len(words)
    opened_file.close()
    result.append(num_lines)
    result.append(num_words)
    return result
    
print(num_lines_words('obama_speech.txt'))
print(num_lines_words('michelle_obama_speech.txt'))

# find most spoken languages in data dictionary
import json
from collections import Counter
def most_spoken_languages(filename, num):
    opened_file = open(filename)
    countries_dict = json.load(opened_file)
    c = Counter()
    unique_lang = []
    index = 0
    for index in range(len(countries_dict)):
        languages = countries_dict[index]['languages']
        for l in languages:
            if l not in unique_lang:
                c[l] = 1
                unique_lang.append(l)
            else:
                c[l] += 1
        index += 1
    most_spoken = c.most_common(num)
    return most_spoken

print(most_spoken_languages('countries_data.json', 10))
print(most_spoken_languages('countries_data.json', 3))

    
    