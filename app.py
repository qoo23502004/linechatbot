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
line_bot_api = LineBotApi('s49cl/eWlu7yCPyUa4nZ+RruopYWFYgPRfku997PeI/yiBGDzaQno/RlFs+PgR6Fn/ggaPRXrqBAffTuaasCKQz1PqJN74fMDCYwaHHqNoHZ3Aykp2YJBY8P7h2xetX+UsUbBrZJb4gRUPvXj0a3IgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a79317aa1170b94d6c98d402d603c7c6')

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
    feed=["!早餐","!午餐","!下午茶","!晚餐","!宵夜","!消夜"]

    ytKeyword=""
    if event.message.text=="!HI":
        message = TextSendMessage(text="Hi^^")
        line_bot_api.reply_message(event.reply_token, message)
    
    if event.message.text=="!狀態":
        string = checkState()
        message = TextSendMessage(text=string)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text in cityDict:
        string = weatherSearch(event.message.text)
        message = TextSendMessage(text=string)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text in feed:
        string = food(event.message.text)
        message = TextSendMessage(text="真心推薦: "+string)
        line_bot_api.reply_message(event.reply_token, message)
    
    keyword=event.message.text
    keywordCut=keyword.split(' ')
    if keywordCut[0]=="!sr" and len(keywordCut)>=2:
        for i in range(1,len(keywordCut)):	
            ytKeyword=ytKeyword+keywordCut[i]+" "
        content = musicSearch(ytKeyword)
        message = TextSendMessage(text="https://www.youtube.com/watch?v="+content)
        line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
