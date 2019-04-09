import warnings
warnings.filterwarnings('ignore')
import copy
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pprint

def scraper(url, mongo_path, tag, column_list):
    '''
    We're going to scrape some crime data from a site.
    
    Inputs:
    url: string of url to the webpage that our table is on
    mongo_path: string with the path to our Mongo DB.  ex: 'mongodb://localhost:27017'
    tag: string of div tag for the table.  ex: 'table-responsive'
    column_list: a list of columns in the table we're scraping in the order they appear
    
    Output: 
    a Pandas DF
    '''
    
    # send a GET request and store content 
    r = requests.get(url)
    client = MongoClient(mongo_path)
    db = client.metroid # can be set to any client.
    pages = db.pages
    pages.insert_one({'html': r.content})

    # use Beautiful Soup to parse HTML to Python Object
    soup = BeautifulSoup(r.content, 'lxml')
    soup.prettify()
    
    # sift through our data and pull the table we want
    div = soup.find('div', {'class':tag})
    table = div.find('table')
    
    # create an iterator and accumulator to go over each row in the table
    rows = table.find_all('tr')
    all_rows = []

    # store each column as a dictionary
    empty_row = {}
    for i in column_list:
        empty_row[i] = None
    empty_row

    # fill our column dictionary, but skip headers
    for row in rows[1:]:
        new_row = copy.copy(empty_row)
        columns = row.find_all('td')
        for i, row in enumerate(column_list):
            new_row[row] = columns[i].text.strip()
        all_rows.append(new_row)
    
    # load rows into Mongo DB
    crime_rate = db.crime_rate
    for row in all_rows:
        crime_rate.insert_one(row)
    
    # load rows into Pandas DF
    rows = crime_rate.find()
    crime_rates = pd.DataFrame(list(rows))
    return crime_rates.head()