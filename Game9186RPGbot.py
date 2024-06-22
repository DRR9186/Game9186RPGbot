import telebot
from telebot import types

bot = telebot.TeleBot('7169453337:AAEVj-MtM28feLTotVaJUHd20LTx3MgJzA8')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    
    reg = types.KeyboardButton('начать игру')
    
    markup.add(reg)
    bot.send_message(message.chat.id, 'Добро пожаловать в Реактариум!'.format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def reg(message):
    if message.text == 'начать игру':
        msg = bot.send_message(message.chat.id, 'Введите своё имя')
        bot.register_next_step_handler(msg, username)
        
def username(message):
    name = message.text
    bot.send_message(message.chat.id, 'приятно познакомиться, ' + name)
    markup = types.ReplyKeyboardMarkup()
    
    res = types.KeyboardButton('добыча ресурсов')
    hunt = types.KeyboardButton('Охота')
    trade = types.KeyboardButton('Торговля')
    markup.add(res,hunt,trade)
    
    bot.send_message(message.chat.id, 'Статус игрока ' + name .format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def res(message):
    if message.text == 'добыча ресурсов':
        bot.send_message(message.chat.id, 'Выберите ресурс')

bot.polling(none_stop=True, interval = 0)