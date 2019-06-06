import json
import pandas as pd
import re
import datetime as datetime
import requests
import csv
from newspaper import Article
from bs4 import BeautifulSoup
from csv import reader
from random import *
import time
'''
jan_2016_Google_Search_Articles.csv, feb_2016_Google_Search_Articles.csv, mar_2016_Google_Search_Articles.csv, apr_2016_Google_Search_Articles.csv,
may_2016_Google_Search_Articles.csv, jun_2016_Google_Search_Articles.csv, jul_2016_Google_Search_Articles.csv, aug_2016_Google_Search_Articles.csv
sep_2016_Google_Search_Articles.csv, oct_2016_Google_Search_Articles.csv, nov_2016_Google_Search_Articles.csv, dec_2016_Google_Search_Articles.csv
'''
month ="12"

filename = 'dec_2016_Google_Search_Articles.csv'
Aritle_URLs = []
import webbrowser

def title_create(title):
# opens a csv file and grabs the URL of the article
    with open(title) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_type = row['Type']
            url = row['URL']
            if row_type != 'None':
                #print(url)
                Aritle_URLs.append(url)




title_create(filename)

Article_Date = []
Article_Title = []
count = 1
for url in Aritle_URLs:

    print("Number : ",count)
    article = Article(url)
    article.download()
    if article.download_state == 0:
        print("Retrying in 25 seconds!!")
        time.sleep(25)
        article.download()
    if article.download_state != 1:
        print("GOOD")
        article.parse()
        dated = str(article.publish_date)
        if dated != 'None':
            the_date = (dated[:10])
            the_date = datetime.datetime.strptime(the_date,'%Y-%M-%d').strftime('%m/%d/%Y')
            fixed_date = month + the_date[2:10]
            print(fixed_date)
        if dated == 'None':
            fixed_date = dated
            webbrowser.open(url)

        title = article.title
        Article_Date.append(fixed_date)
        Article_Title.append(title)
        print(title)
        count = count + 1


    print(url)
newrowlist = []
rownames = ["Date", "Title", "Type/Value","Blank", "URL"]
newrowlist.append(rownames)
z = 0
while (z <= (len(Article_Date)-1)):
    newrow = [Article_Date[z],
                Article_Title[z],
                "n", 0, Aritle_URLs[z],]

    newrowlist.append(newrow)
    z = z + 1
new_title = filename[:31] + "_Titled.csv"
file = open(new_title, 'w')
writer = csv.writer(file)
writer.writerows(newrowlist)
file.close()
