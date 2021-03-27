#!/usr/bin/env python3
# -*- conding: utf-8 -*-
import requests
import telepot
import os
import pandas as pd
import pandas_datareader as pdr

from bs4 import BeautifulSoup

def SendTelegramMsg(msg) :
	token= "1354983269:AAGwZkkvUZkQ567vqcvkvzbV3E2wUFabMW8"
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
            base_url = 'https://m.stock.naver.com/item/main.nhn#/stokcs/'
            print('title = ' + title)
            print('name = ' + name)
            code = getFinanceCode(name)
            print('news_link:'+news_link+'\n')
            msg = title + '\n' + news_link
            if is_int(code):
                msg += '\n' + base_url + code + '/total'

            SendTelegramMsg(msg)
            with open(os.path.join(BASE_DIR, 'compare.txt'), 'a') as f_write:
                f_write.write(news_link+'\n')
                f_write.close()

# 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
def get_code(df, name):
    code_temp = df.query("name=='{}'".format(name))['code'].to_string(index=False)
    # 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript() 하여 공백 제거
    code_temp = code_temp.strip()
    return code_temp

def getFinanceCode(name):
    df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
    df = df[['회사명', '종목코드']]
    df = df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    df.code = df.code.map('{:06d}'.format)
    code_temp = get_code(df, name)
    print('code = ' + code_temp)
    return code_temp

def is_int(val):
   return val.lstrip("-+").isdigit()
 
lv1_url = 'https://m.sedaily.com/Search/Search/SEList?Page=1&scDetail=&scOrdBy=0&catView=AL&scText=&scjText=%EC%96%91%ED%95%9C%EB%82%98&scPeriod=6m&scArea=tc&scTextIn=&scTextExt=&scPeriodS=&scPeriodE=&command=&ViewCnt=10&_=1599581418086'
html = requests.get(lv1_url).text
soup = BeautifulSoup(html, 'html.parser')
 
for a_tag in soup.select('a'):
	title = a_tag['title']
	link = 'https://m.sedaily.com'+a_tag['href']
	Compare(link)
	#print(a_tag.text, link)
