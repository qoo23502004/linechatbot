from flask import Flask, request, abort
from bs4 import BeautifulSoup
from botFunction import *
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import time

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('09mdileCjp5VlcpNG1gv+3gZ2tBa0tcBGNbzQEwPcZbVYqfTCXPkbuebN7In2nPC7adVZKiHKJHfvO5ZmwjBBSXW/4gvzOuZzbGfeAP0fqGtJxM3j+VFX6Ac2L8g/N3RyQJ2qusyx5s0nkRfPQHozQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('994cd15223d21d1114738fa4b6111b42')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    cityDict={"!嘉義縣":0,"!新北市":1,"!嘉義市":2,"!新竹縣":3,"!新竹市":4,"!台北市":5,"!台南市":6,"!宜蘭縣":7,"!苗栗縣":8,"!雲林縣":9,"!花蓮縣":10,"!台中市":11,"!台東縣":12,"!桃園市":13,"!南投縣":14,"!高雄市":15,"!金門縣":16,"!屏東縣":17,"!基隆市":18,"!澎湖縣":19,"!彰化縣":20,"!連江縣":21}
    food=["!早餐","!午餐","!下午茶","!晚餐","!宵夜","!消夜"]

    ytKeyword=""
    pushAns=""
	
    if event.message.text=="咬咬":
        #profile = line_bot_api.get_profile(event.source.user_id)
        message = TextSendMessage(text="找我幹嘛呢?")
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text=="!序號":
        #profile = line_bot_api.get_profile(event.source.user_id)
        message = TextSendMessage(text="◎序號兌換至myVideo官網/APP「兌換儲值」輸入序號 「vv0z1」兌換使用\nhttps://reurl.cc/XjRx3")
        line_bot_api.reply_message(event.reply_token, message)
    
    if event.message.text=="!狀態":
        string = checkState()
        message = TextSendMessage(text=string)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text in cityDict:
        profile = line_bot_api.get_group_member_profile(event.source.group_id,event.source.user_id)       
        string = weatherSearch(event.message.text)
        message = TextSendMessage(text="To "+profile.display_name+"\n"+string)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text in food:
        string = food(event.message.text)
        message = TextSendMessage(text="真心推薦: "+string)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text=="!GID":           
        message = TextSendMessage(text=event.source.group_id)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text=="!RID":                  
        message = TextSendMessage(text=event.source.room_id)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text=="!UID":                  
        message = TextSendMessage(text=event.source.user_id)
        line_bot_api.reply_message(event.reply_token, message)

    ans=event.message.text
    ansCut=ans.split(' ')
    if ansCut[0]=="!意見" and len(ansCut)>=2:
        for i in range(1,len(ansCut)):
            pushAns=pushAns+ansCut[i]+" "
        profile = line_bot_api.get_group_member_profile(event.source.group_id,event.source.user_id)      
        line_bot_api.push_message("C4917ea14175c364153551090ab546fd5", TextSendMessage(text="來自 "+profile.display_name+" 的訊息： "+ pushAns))
        #message = TextSendMessage(text=event.source.user_id)
        #line_bot_api.reply_message(event.reply_token, message) 
    
    keyword=event.message.text
    keywordCut=keyword.split(' ')
    if keywordCut[0]=="!sr" or keywordCut[0]=="!SR" and len(keywordCut)>=2:
        for i in range(1,len(keywordCut)):	
            ytKeyword=ytKeyword+keywordCut[i]+" "
        content = musicSearch(ytKeyword)
        message = TextSendMessage(text="https://www.youtube.com/watch?v="+content)
        line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
