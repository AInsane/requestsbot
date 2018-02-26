
import time
import config
import telebot


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands= ['start', 'help'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hi ! How are you?=)')

@bot.message_handler(func = lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)




if __name__ == '__main__':
    bot.polling(none_stop = True)