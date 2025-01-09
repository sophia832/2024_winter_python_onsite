from flask import (
    Flask,
    request,
    abort
)
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,  # 傳輸回Line官方後台的資料格式
)
from linebot.v3.webhooks import (
    MessageEvent,  # 傳輸過來的方法
    TextMessageContent,  # 使用者傳過來的資料格式
)

import os

app = Flask(__name__)
handler = WebhookHandler(os.getenv('LINEBOT_SECRET_KEY'))
configuration = Configuration(access_token=os.getenv('LINEBOT_ACCESS_TOKEN'))


@app.route("/callback", methods=['POST'])
def callback():
    # 設計一個 callback 的路由，提供給Line官方後台去呼叫
    # 也就所謂的呼叫Webhook Server
    # 因為官方會把使用者傳輸的訊息轉傳給Webhook Server
    # 所以會使用 RESTful API 的 POST 方法

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    # user_id = event.source.user_id  # 使用者的ID，未來管理歷史訊息可以用
    user_message = event.message.text  # 使用者傳過來的訊息

    if user_message == "本日新聞摘要":
        responses = [
            TextMessage(text="此處應由爬蟲爬取結果後，交由ChatGPT擷取摘要，再回傳給使用者")
        ]
    else:
        responses = [
            TextMessage(text="抱歉，我是一個新聞摘要機器人，您可以輸入'新聞摘要'來取得本日的新聞資訊。")
        ]
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=responses
            )
        )


if __name__ == "__main__":
    app.run(debug=True)
