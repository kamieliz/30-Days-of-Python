# import modules for web scraping
import requests
from bs4 import BeautifulSoup
import json

# website to scrape
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# used to fetch data from url
response = requests.get(url)
# get all the content from site
content = response.content

# Beautiful soup will parse content
soup = BeautifulSoup(content, 'html.parser')
totalScrapedInfo = []
totalScrapedInfo.append(str(soup.title))
totalScrapedInfo.append(str(soup.body))

# create json file to save scraped data
file = open('bu_facts.json', mode='w', encoding='utf-8')
# save data to json file
file.write(json.dumps(totalScrapedInfo))

# extract table from another url and change into a json file
url1 = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url1)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# find table object from inspection the table we want is at cellpadding = 3
tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0]
table_data = []
for td in table.find('tr').find_all('td'):
    table_data.append(td.text)

file = open('uci_table.json', mode='w', encoding='utf-8')
file.write(json.dumps(table_data))