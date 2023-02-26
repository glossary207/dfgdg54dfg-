import openai
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# กำหนด API key ของ OpenAI
openai.api_key = "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"

# กำหนด Channel access token และ Channel secret ของ Linebot
line_bot_api = LineBotApi('GKSxNLQax9VoiJMVsQ3pxwMjoZuAjGBap1jlaQu8iyAu4VbMezv0/ReMK2YJEZU6VSWN9d52htbN6NWf516fzOiMW9BBLLGIeKPmhMl+gw+3ToEsJMsnmeUmq2ckDH5zoJYUwSaeYWY4goloqMmtfAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('77f97ba29e10e6442381bdca9f4a5d0b')

# กำหนดฟังก์ชันสำหรับการตอบแชท
def generate_response(input_text):
    # เรียกใช้ API ของ OpenAI เพื่อสร้างคำตอบแชท
    prompt = "The following is a conversation with a chatbot. The bot is helpful, creative, clever, and very friendly. " + input_text + "\nBot:"
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5,
    )
    return response.choices[0].text.strip()

# กำหนดฟังก์ชันสำหรับการรับข้อความและตอบกลับ
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text
    output_text = generate_response(input_text)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text=output_text)
    )

# รันโค้ดบน Heroku server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
