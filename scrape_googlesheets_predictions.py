import datetime
import time
import os

from urllib.request import urlretrieve

#target url for rotogrinder nba player projections
url = 'https://docs.google.com/spreadsheets/d/1F6tRt7uAJGyNmgitJbBeb-7BGkqzeOH3-VJnHlBTyPo/edit#gid=54487280'
destination = 'googlesheets_predictions.csv'

#scraping function for target url
def scrape_googlesheets_predictions():
    urlretrieve(url, destination)
