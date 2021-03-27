#!/usr/bin/env python3
import requests
import telepot
import os
import sys

from bs4 import BeautifulSoup

def SendTelegramMsg(msg) :
	token= "1354983269:AAGwZkkvUZkQ567vqcvkvzbV3E2wUFabMW8"
	mc = "-1001357961262"	#channel
	bot = telepot.Bot(token)

	bot.sendMessage(mc, msg)

def Compare(title, news_link):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/db'
    with open(os.path.join(BASE_DIR, 'hotdeal_ppomppu.txt'), 'r')as f_read:
        before = f_read.readlines()
        before = [line.rstrip() for line in before] #(\n)strip in list

        f_read.close()
        if news_link not in before:
            SendTelegramMsg(str(title) + '\n' + news_link)
            print('title = ', title)
            print('news_link:'+news_link+'\n')
            with open(os.path.join(BASE_DIR, 'hotdeal_ppomppu.txt'), 'a') as f_write:
                f_write.write(news_link+'\n')
                f_write.close()

def main(key):    
    lv1_url = 'http://m.ppomppu.co.kr/new/bbs_list.php?id=ppomppu&category=&search_type=subject&keyword='+key
    html = requests.get(lv1_url).text
    soup = BeautifulSoup(html, 'html.parser')

    board = soup.find('div', class_='bbs')
    border = board.find_all('li', class_='none-border')
    #print(board)
     
    for a_tag in border:
        #print(a_tag)
        tag = a_tag.find('a')
        link = 'http://m.ppomppu.co.kr/new/' + tag['href']
        title = a_tag.find('span', class_='cont').text
        if title :
            print(title, link)
            Compare(title, link)
        #print(a_tag.text, link)


if __name__ == '__main__':
    main(sys.argv[1])
