from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
import datetime

#web scraping

url = 'https://www.timeanddate.com/weather/'
res = requests.get(url).content
soup = BeautifulSoup(res,'html.parser')

#home view
def home(requests,soup=soup):
    date = datetime.datetime.now()
    data = soup.find('span',class_='my-city__city')
    data1 = soup.find('span',class_='my-city__temp')
    kill="MADHU_GEEKS"

    city = data.text
    temp = data1.text

    return render(requests,'index.html',{'city':city,'temp':temp,'date':date,'kill':kill})
