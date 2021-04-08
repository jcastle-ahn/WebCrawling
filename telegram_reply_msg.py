import time
import telepot
import os

f = open('/home/ubuntu/crawling/token.txt', mode='rt', encoding='utf-8')
token = f.read().splitlines()[0]
bot = telepot.Bot(token)

InfoMsg = "아래의 요청 중 하나를 고르고 번호를 입력하세요.\n" \
          "1. 주가 확인\n" \
          "2. 환율 확인\n" \
          "3. 날씨 확인\n" \
          "4. 종료"

status = True

def handle(msg):
    content, chat, id = telepot.glance(msg)
    print(content, chat, id)  # 텔레그램에 입력되는 메세지의 타입, 채팅 타입, 메세지 송신 ID

    if content == 'text':
        if msg['text'] == '1':
            bot.sendMessage(id, '주가를 확인합니다.')
        elif msg['text'] == '2':
            bot.sendMessage(id, '환율을 확인합니다.')
        elif msg['text'] == '3':
            bot.sendMessage(id, '날씨를 확인합니다.')
        elif msg['text'] == '4':
            bot.sendMessage(id, 'Bye~')
            os._exit(1) # 스크립트 강제 종료
        else:
            bot.sendMessage(id, InfoMsg)

bot.message_loop(handle)

while status == True:
    time.sleep(10)