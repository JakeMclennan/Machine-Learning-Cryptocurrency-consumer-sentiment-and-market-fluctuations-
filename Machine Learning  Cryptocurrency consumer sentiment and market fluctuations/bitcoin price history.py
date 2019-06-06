import pandas as pd
import quandl
import math
import numpy as np
from pandas import Index
df = quandl.get('BNC3/GWA_BTC')
import bs4 as bs
import requests
import csv
import datetime as dt
import pandas_datareader.data as web
from csv import reader
from dateutil import parser

                                    # I would adjust daate range by changing the start= and end= in weburl
weburl = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130828&end=20171029'
newrowlist = []
resp = requests.get(weburl)
soup = bs.BeautifulSoup(resp.text, "html.parser")
table = soup.find('table', {'class': 'table'})
BTC_open = 0
BTC_close = 0
Percent_change = 0 
Dates = []
Openings = []
rownames = ["Date", "Open", "High", "Low", "Close", "Volume", "Market Cap", "Percent Change"]
newrowlist.append(rownames)
for row in table.find_all('tr')[1:]:
    BTC_open = float(row.find_all('td')[1].text)
    BTC_close = float(row.find_all('td')[4].text)
    Percent_change = (((BTC_close - BTC_open)/(BTC_open))* 100)
    PC = round(Percent_change,2)
    newrow = [row.find_all('td')[0].text, 
    row.find_all('td')[1].text,
    row.find_all('td')[2].text,
    row.find_all('td')[3].text,
    row.find_all('td')[4].text,
    row.find_all('td')[5].text,
    row.find_all('td')[6].text,
    #Percent_change]
    PC]
    newrowlist.append(newrow)


    
file2 = open("bitcoin_history.csv", 'w')
writer = csv.writer(file2)
writer.writerows(newrowlist)
file2.close()

