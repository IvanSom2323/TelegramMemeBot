import telebot
import os, random
bot = telebot.TeleBot('7830873919:AAECfhavPYiQ2Pvs196npr5sVmuLC2X1FBo')
@bot.message_handler(commands=['meme'])
def send_meme(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Впиши команду /meme и получиш мем!')
bot.polling()
