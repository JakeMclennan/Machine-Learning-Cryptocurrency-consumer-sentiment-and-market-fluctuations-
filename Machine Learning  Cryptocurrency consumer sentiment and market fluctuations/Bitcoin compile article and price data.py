import json
import chardet
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
Article_Date_List = []
Title_List = []
Value_List = []
Type_List = []
Url_List = []




'''
Price_Date_list = []
Open_list = []
High_list = []
Low_list = []
Close_list = []
Volume_list = []
Market_Cap_list = []
Percent_Change_list = []'''

Price_Date_list = []
Open_list = {}
High_list = {}
Low_list = {}
Close_list = {}
Volume_list = {}
Market_Cap_list = {}
Percent_Change_list = {}





Article_name = 'Google_2017_Titled.csv'
Price_name = 'Bitcoin_2017_Price_data.csv'
def Article_get(name):
# opens a csv file and grabs the URL of the article
    with open(name, encoding='UTF-8') as csvfile:
    #with open(name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rDate = row['Date']
            rTitle = row['Title']
            rValue = row['Value']
            rType = row['Type']
            rURL = row['URL']
            
            #rDate = datetime.strptime(rDate, '%b/%d/%Y')
            #print(rDate)
            Article_Date_List.append(rDate)
            Title_List.append(rTitle)
            Value_List.append(rValue)
            Type_List.append(rType)
            Url_List.append(rURL)
def remove_zero(rDate):
    
    #print(rDate[:3])
    #print(rDate[2:3])
    #print(rDate[:2])
    if rDate[2:3] == "0":
        new_date = str(rDate[:2]+rDate[3:4]+rDate[4:])
        return new_date

    if rDate[2:3] == "/":
        if rDate[3:4] == "0":
            #print("----------")
            #print(rDate[4:5])
            new_date = str(rDate[:3]+rDate[4:5]+rDate[5:])
            return new_date
            #print(new_date)
            #print(rDate)
        else:
            return rDate
    else:
        return rDate

def Price_get(name):
    with open(name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rDate = row['Date']
            rOpen = row['Open']
            rHigh = row['High']
            rLow = row['Low']
            rClose = row['Close']
            rVolume = row['Volume']
            rMarket_Cap = row['Market Cap']
            rPercent_Change = row['Percent Change']
            rDate = remove_zero(rDate)
            print(rDate)
            Price_Date_list.append(rDate)
            Open_list.update({rDate:float(rOpen)})
            High_list.update({rDate:float(rHigh)})
            Low_list.update({rDate:float(rLow)})
            Close_list.update({rDate:float(rClose)})
            Volume_list.update({rDate:rVolume})
            Market_Cap_list.update({rDate:rMarket_Cap})
            Percent_Change_list.update({rDate:float(rPercent_Change)})






            
Article_get(Article_name)
Price_get(Price_name)

newrowlist = []
rownames = ["Date", "Title", "Value", "Type", "URL" ,"Open", "High", "Low", "Close", "Volume", "Market Cap", "Percent Change"]
newrowlist.append(rownames)
z = 0
#print("Here")
while (z <= (len(Article_Date_List)-1)):

    article_date = Article_Date_List[z]

    newrow = [Article_Date_List[z], Title_List[z], Value_List[z],Type_List[z], Url_List[z],
              Open_list[article_date], High_list[article_date], Low_list[article_date], Close_list[article_date], Volume_list[article_date], Market_Cap_list[article_date], Percent_Change_list[article_date]]
    newrowlist.append(newrow)
    z = z + 1

for pd in Price_Date_list:
    if pd not in Article_Date_List:
            newrow = [pd, "VOID", "VOID","VOID", "VOID",
              Open_list[pd], High_list[pd], Low_list[pd], Close_list[pd], Volume_list[pd], Market_Cap_list[pd], Percent_Change_list[pd]]
            newrowlist.append(newrow)
    

    

new_title = "2017 all compiled.csv"
file = open(new_title, 'w', encoding='UTF-8')
writer = csv.writer(file)
writer.writerows(newrowlist)
file.close()

