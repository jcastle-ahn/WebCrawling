#!/usr/bin/env python3
import requests
import telepot
import os

from bs4 import BeautifulSoup

def SendTelegramMsg(msg) :
	f = open('/home/ubuntu/crawling/token.txt', mode='rt', encoding='utf-8')
	token = f.read().splitlines()[0]
	mc = "-1001218462501"	#channel
	bot = telepot.Bot(token)

	bot.sendMessage(mc, msg)

def Compare(news_link):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/db'
    with open(os.path.join(BASE_DIR, 'compare.txt'), 'r')as f_read:
        before = f_read.readlines()
        before = [line.rstrip() for line in before] #(\n)strip in list

        f_read.close()
        if news_link not in before:
            name = title.split(',')
            name = name[0]
            name = name[5:]		#remove [SEN]
            SendTelegramMsg(title + '\n' + news_link)
            print('title = ' + title)
            print('name = ' + name)
            print('news_link:'+news_link+'\n')
            with open(os.path.join(BASE_DIR, 'compare.txt'), 'a') as f_write:
                f_write.write(news_link+'\n')
                f_write.close()
 
lv1_url = 'https://m.sedaily.com/Search/Search/SEList?Page=1&scDetail=&scOrdBy=0&catView=AL&scText=&scjText=%EC%96%91%ED%95%9C%EB%82%98&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=&command=&ViewCnt=10&_=1599581418086'
html = requests.get(lv1_url).text
soup = BeautifulSoup(html, 'html.parser')
 
for a_tag in soup.select('a'):
	title = a_tag['title']
	link = 'https://m.sedaily.com'+a_tag['href']
	Compare(link)
	#print(a_tag.text, link)
