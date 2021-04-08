#!/usr/bin/env python3
import requests
import telepot
import os
import sys

from datetime import datetime
from bs4 import BeautifulSoup

def SendTelegramMsg(msg) :
	f = open('/home/ubuntu/crawling/token.txt', mode='rt', encoding='utf-8')
	token = f.read().splitlines()[0]
	mc = "-1001370161647"	#channel
	bot = telepot.Bot(token)

	bot.sendMessage(mc, msg)

def Compare(title, link, state):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/db'
    with open(os.path.join(BASE_DIR, 'imsang.txt'), 'r')as f_read:
        before = f_read.readlines()
        before = [line.rstrip() for line in before] #(\n)strip in list

        f_read.close()
        find_str = state+link
        #print('find_str =', find_str)
        #for text in before:
        #    print('text =', text)

        if find_str not in before:
            SendTelegramMsg(str(title) + '\n' + link)
            print('title = ', title)
            print('link:'+link+'\n')
            with open(os.path.join(BASE_DIR, 'imsang.txt'), 'a') as f_write:
                f_write.write(find_str+'\n')
                f_write.close()

def main():    
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    day_string = str(year) + '-' + str(month) + '-' + str(day)
    print('day_string =', day_string)
    url = 'https://nedrug.mfds.go.kr/searchClinic?page=1&searchYn=true&approvalStart=&approvalEnd=&searchType=ST3&searchKeyword='
    url += '&approvalDtStart='+day_string+'&approvalDtEnd='+day_string
    url += '&clinicStepCode=&examFinish=&domestic=&gender=&age=&localList=000&localList2='
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    board = soup.find('table', class_='dr_table dr_table_type2')
    #print(board)
     
    count = 0
    send_msg = ''
    link = 'https://nedrug.mfds.go.kr'
    state = ''
    for a_tag in board.select('td'):
        print(a_tag.text)
        send_msg += a_tag.text + '\n'
        count+=1
        if (count%9 == 0):
            print()
            Compare(send_msg, link, state)
            send_msg = ''
            link = 'https://nedrug.mfds.go.kr'
        elif (count%9 == 5):
            link += a_tag.find('a')['href']
            print('link', link)
        elif (count%9 == 2):
            state = a_tag.text.rstrip().lstrip()
            print('state', state)

if __name__ == '__main__':
    main()
