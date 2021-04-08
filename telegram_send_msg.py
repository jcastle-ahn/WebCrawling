#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telepot

def sendTelegramMsg(msg) :
	f = open('/home/ubuntu/crawling/token.txt', mode='rt', encoding='utf-8')
	token = f.read().splitlines()[0]
	mc = "719701722"	#jcastle
	#mc = "-1001357961262"	#channel
	bot = telepot.Bot(token)

	bot.sendMessage(mc, msg)

sendTelegramMsg("안녕.")
