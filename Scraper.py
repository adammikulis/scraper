# -*- coding: utf-8 -*-
"""
By: Adam Mikulis
20191217
Class to scrape for prices
"""

import requests, bs4, os
import pandas as pd


class Scraper:
    
    # Init function
    def __init__(self):
        pass
    
    # Load spreadsheet of items into dataframe
    def load_items(self, filepath='/home/adam/Downloads/scraping/', filename='fao_items.csv', ):
        self.item_chart = pd.read_csv(filepath+filename)
        return self.item_chart
    
    # Pull a specific column of data
    def pull_column(self, column_name='UPC'):
        self.column_data = self.item_chart[column_name]
        return self.column_data
    
    # Get data from website
    def pull(self, url):
        self.url = url
        self.content = requests.get(self.url)
        return self.content
    
    # Convert data to parsible format
    def soupify(self):
        self.content = bs4.BeautifulSoup(self.content.text, features='html.parser')
        return self.content

class FAO(Scraper):
    def __init__(self):
        pass

    # Calls all 'find' functions
    def find_all(self):
        self.find_title()
        self.find_price()

    # Pull title
    def find_title(self):
        self.title = self.content.title.string
        return self.title
    
    # Pull price
    def find_price(self):
        self.price = self.content.find('span', {'class': 'price'}).string
        return self.price
    
    def find_item_no(self):
        self.item_no = self.content.find('div', {'class': 'itemid'})
        return self.item_no
    
    # Remove $ and convert to float
    def convert_price(self):
        self.price = float(self.price.replace('$', ''))
        return self.price
    
    # Load all data into dictionary
    def load_dict(self):
        self.dict = {
            'title' : self.title,
            'price' : self.price}
        return self.dict


url = 'https://www.firstaidonly.com/first-aid-refills/first-aid-kit-refills/adhesive-bandages/fabric/1-x3-fabric-bandages-50-per-box.html'
ex = FAO()
ex.load_items()
df = ex.item_chart
ex.pull(url)
ex.soupify()
#ex.find_all()
#ex.convert_price()
#ex.load_dict()
ex.find_item_no()
print(ex.item_no)