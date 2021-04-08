#!/usr/bin/env python3
import requests
import telepot

from bs4 import BeautifulSoup

def sendTelegramMsg(msg) :
	f = open('/home/ubuntu/crawling/token.txt', mode='rt', encoding='utf-8')
	token = f.read().splitlines()[0]
	mc = "719701722"
	bot = telepot.Bot(token)

	bot.sendMessage(mc, msg)
 
lv1_url = 'https://m.sedaily.com/Search/Search/SEList?Page=1&scDetail=&scOrdBy=0&catView=AL&scText=&scjText=%EC%96%91%ED%95%9C%EB%82%98&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=&command=&ViewCnt=10&_=1599581418086'
html = requests.get(lv1_url).text
soup = BeautifulSoup(html, 'html.parser')

count = 0
 
for a_tag in soup.select('a'):
	if count == 0 :
		sendTelegramMsg('https://m.sedaily.com'+a_tag['href'])
		count = 1
	print(a_tag.text, 'https://m.sedaily.com'+a_tag['href'])
