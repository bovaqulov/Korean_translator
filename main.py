
import threading
import time
import schedule
from googletrans import Translator
from telebot import TeleBot
from telebot.types import Message
from trans import EasyGoogleTranslate

bot = TeleBot("<your_telegram_api>", parse_mode="html")

text_start = ("Hello. Just translate."
               "Language setting removed.\n\n"
               "The bot itself chooses the language to be translated")


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text_start)


@bot.message_handler(content_types=['text'])
def user_text(message: Message):
    chat_id = message.chat.id
    translator = Translator()
    lang = translator.detect(message.text)
    lange = lang.lang
    if lange == 'ko':
        texte = EasyGoogleTranslate().translate(message.text, source_language="ko", target_language="uz")
    else:
        texte = EasyGoogleTranslate().translate(message.text, source_language="uz", target_language="ko")
    bot.send_message(chat_id, texte)

if __name__ == '__main__':
    print("welcome ... ")
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
