import warnings
warnings.filterwarnings('ignore')

import copy
import pandas as pd

# Requests sends and recieves HTTP requests.
import requests

# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup

# imports related to MongoDB
from pymongo import MongoClient
import pprint

# Send a GET request for the data
port_crime_url = 'http://www.city-data.com/crime/crime-Portland-Oregon.html'
r = requests.get(port_crime_url)

# check to see if it worked; 200 is good
r.status_code

# check our raw hypertext
r.content

# save hypertext into mongo for use later
client = MongoClient('mongodb://localhost:27017/')
db = client.portcrime
pages = db.pages

pages.insert_one({'html': r.content})

# Parse html into a Python object
soup = BeautifulSoup(r.content,'lxml')
print(soup.prettify())

# navigate through data and pull out the table we are looking for
div = soup.find('div', {'class':'table-responsive'})
table = div.find('table')

# create an iterator to go over each row in the table
rows = table.find_all('tr')

# an empty accumulator 
all_rows = []

# store each column as a dictionary
empty_row = {
    'type': None,
    '2003': None,
    '2004': None,
    '2005': None,
    '2006': None,
    '2007': None,
    '2008': None,
    '2009': None,
    '2010': None,
    '2011': None,
    '2012': None,
    '2013': None,
    '2014': None,
    '2016': None,
    '2017': None
}

# fill our columns, but skip the first row of headers
for row in rows[1:]:
    new_row = copy.copy(empty_row)
    # A list of all entries in the row
    columns = row.find_all('td')
    new_row['type'] = columns[0].text.strip()
    new_row['2003'] = columns[1].text.strip()
    new_row['2004'] = columns[2].text.strip()
    new_row['2005'] = columns[3].text.strip()
    new_row['2006'] = columns[4].text.strip()
    new_row['2007'] = columns[5].text.strip()
    new_row['2008'] = columns[6].text.strip()
    new_row['2009'] = columns[7].text.strip()
    new_row['2010'] = columns[8].text.strip()
    new_row['2011'] = columns[9].text.strip()
    new_row['2013'] = columns[10].text.strip()
    new_row['2012'] = columns[11].text.strip()
    new_row['2014'] = columns[12].text.strip()
    new_row['2016'] = columns[13].text.strip()
    new_row['2017'] = columns[14].text.strip()
    all_rows.append(new_row)

# load the rows into our Mongo DB
port_crime = db.port_crime
for row in all_rows:
    port_crime.insert_one(row)

# load rows from Mongo to check
rows = port_crime.find()
portland_crime = pd.DataFrame(list(rows))
portland_crime.head()

# rearrange some columns
portland_crime = portland_crime.drop('_id',axis=1)
portland_crime = portland_crime.set_index('type')
portland_crime.head()
