from telebot.types import Message
from main import bot
from gtts import gTTS
import os


@bot.message_handler(commands=['audio'])
def text_to_audio(message: Message):
    text = message.text.replace('/text_to_audio', '', 1).strip()

    tts = gTTS(text=text, lang='ko')
    tts.save('output.mp3')

    # Send the audio file to the user
    audio = open('output.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()

    # Delete the temporary audio file
    os.remove('output.mp3')
