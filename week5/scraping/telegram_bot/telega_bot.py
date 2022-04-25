import telebot
import csv
from MyToken import token
from telebot import types

# inlineKeyboardMarkup
# replyKeyboardMarkup

bot = telebot.TeleBot(token)

entry = {}

inline_k = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Доход', callback_data='income')
btn2 = types.InlineKeyboardButton('Расход', callback_data='costs')
inline_k.add(btn1, btn2)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет! Сделайте выбор', reply_markup=inline_k)

@bot.callback_query_handler(func=lambda x: True)
def inline(x) : # message
    if x.data == 'income':
        chat_id = x.message.chat.id
        income_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Работа')
        k2 = types.KeyboardButton('Фриланс')
        k3 = types.KeyboardButton('Другое')
        income_k.add(k1,k2,k3)
        msg = bot.send_message(chat_id, 'Выберите категорию', reply_markup=income_k)
        bot.register_next_step_handler(msg, get_category_income)
    elif x.data == 'costs':
        chat_id = x.message.chat.id
        costs_k = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Еда')
        k2 = types.KeyboardButton('Одежда')
        k3 = types.KeyboardButton('Развлечение')
        costs_k.add(k1,k2,k3)
        msg = bot.send_message(chat_id, 'Выберите категорию', reply_markup=costs_k)
        bot.register_next_step_handler(msg, get_category_costs)
def get_category_income(message):
    chat_id = message.chat.id
    entry.update({'category': message.text}) # == entry['category] = message
    msg = bot.send_message(chat_id, 'Укажите сумму')
    bot.register_next_step_handler(msg, get_sum_income)

def get_sum_income(message):
    chat_id = message.chat.id
    entry.update({'sum': message.text})

    file_name = 'income.csv'
    
    with open(file_name, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow( (entry['category'], entry['sum']))

    bot.send_message(chat_id, 'Ваши доходы добавлены', reply_markup=inline_k)



def get_category_costs(message):
    chat_id = message.chat.id
    entry.update({'category': message.text}) # == entry['category] = message
    msg = bot.send_message(chat_id, 'Укажите сумму')
    bot.register_next_step_handler(msg, get_sum_costs)
    
def get_sum_costs(message):
    chat_id = message.chat.id
    entry.update({'sum': message.text})

    file_name = 'costs.csv'
    
    with open(file_name, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow( (entry['category'], entry['sum']))

    bot.send_message(chat_id, 'Ваши расходы добавлены',reply_markup=inline_k)


bot.polling()
#======================================================================

# @bot.message_handler(commands=['start', 'bot'])
# def start_message(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'Привет! Я бот, меня создал Калашович! Если вы из группы ПИ-1-21, то ответье ему "lako"')
#     # user_info = f'{message.from_user.first_name} {message.from_user.username}'

#     # bot.send_message()

# @bot.message_handler(content_types=['sticker', 'text'])
# def send_stiker(message):
#     chat_id = message.chat.id
#     if message.text.lower() == 'hello':
#         bot.send_message(chat_id, 'Hello, my dear!')
#         print(message.text)
#     # bot.send_sticker(chat_id, 'CAACAgIAAxkBAAI5H2JJlE_G2ZhGhcEbdC4wgD4qtFgjAAIcAAPANk8TwYIa0yz-DuEjBA')
# #======================================================================









