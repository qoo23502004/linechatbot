from flask import Flask, request, abort

from linebot import *
from linebot.exceptions import *
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('s49cl/eWlu7yCPyUa4nZ+RruopYWFYgPRfku997PeI/yiBGDzaQno/RlFs+PgR6Fn/ggaPRXrqBAffTuaasCKQz1PqJN74fMDCYwaHHqNoHZ3Aykp2YJBY8P7h2xetX+UsUbBrZJb4gRUPvXj0a3IgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a79317aa1170b94d6c98d402d603c7c6')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
