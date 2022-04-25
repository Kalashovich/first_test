import requests
from bs4 import BeautifulSoup as bs
import csv
import telebot
from telebot import types
from mytoken import token


url = 'https://kaktus.media/?lable=8&date=2022-04-04&order=time'

def get_html(url):
    res = requests.get(url).text
    return res

def get_data(html):
    soup = bs(html, 'lxml')
    data = soup.find_all('div', class_='Tag--article')
    for i in data:
        news = i.find('a', class_='ArticleItem--name').text
        print(news)


get_data(get_html(url))