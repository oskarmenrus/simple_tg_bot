import json
import telebot
import tools
import requests
import urllib.parse

with open('settings.json') as read_file:
    settings = json.load(read_file)

bot = telebot.TeleBot(settings['bot_token'])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_sticker(message.chat.id, open('stickers/cat.webp', 'rb'))
    tools.write_log(message)


@bot.message_handler(commands=['link'])
def lurk_rand_link(message):
    r = requests.get('https://lurkmore.to/Служебная:Random', headers=tools.rheader, proxies=tools.proxies)
    bot.send_message(message.chat.id, f'Случайная ссылка на Луркоморье:\n{urllib.parse.unquote(r.url)}')
    tools.write_log(message)


@bot.message_handler()
def send_kek(message):
    bot.send_message(message.chat.id, 'KEK')
    tools.write_log(message)


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(f'File ID: {message.sticker.file_id}')
    tools.write_log(message)


bot.polling()
