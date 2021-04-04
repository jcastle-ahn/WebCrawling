#!/usr/bin/env python3
import requests
import telepot
import os
import sys

from bs4 import BeautifulSoup

def SendTelegramMsg(msg) :
	f = open('token.txt', mode='rt', encoding='utf-8')
	token = f.read().splitlines()[0]
	mc = "-1001357961262"	#channel
	bot = telepot.Bot(token)

	bot.sendMessage(mc, msg)

def Compare(title, news_link):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/db'
    with open(os.path.join(BASE_DIR, 'hotdeal.txt'), 'r')as f_read:
        before = f_read.readlines()
        before = [line.rstrip() for line in before] #(\n)strip in list

        f_read.close()
        if news_link not in before:
            SendTelegramMsg(str(title) + '\n' + news_link)
            print('title = ', title)
            print('news_link:'+news_link+'\n')
            with open(os.path.join(BASE_DIR, 'hotdeal.txt'), 'a') as f_write:
                f_write.write(news_link+'\n')
                f_write.close()

def main(key):    
    lv1_url = 'https://m.ruliweb.com/market/board/1020?search_type=subject&search_key='+key
    html = requests.get(lv1_url).text
    soup = BeautifulSoup(html, 'html.parser')

    board = soup.find('table', class_='board_list_table')
    #print(board)
     
    for a_tag in board.select('a.subject_link.deco'):
        link = a_tag['href']
        title = a_tag.string
        if title :
            print(title, link)
            Compare(title, link)
        #print(a_tag.text, link)


if __name__ == '__main__':
    main(sys.argv[1])
