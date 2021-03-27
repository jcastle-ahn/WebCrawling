#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telepot

def sendTelegramMsg(msg) :
	token= "1354983269:AAGwZkkvUZkQ567vqcvkvzbV3E2wUFabMW8"
	mc = "719701722"	#jcastle
	bot = telepot.Bot(token)

	bot.sendMessage(mc, msg)

sendTelegramMsg("안녕.")
