
# import telebot
# import os
# from telebot import types


# API_TOKEN = os.environ.get('API_TOKEN')
# bot = telebot.TeleBot(API_TOKEN)

# user_info = {

# }

# glass = {
#     'spring': ['ccna' , 'lpic' , 'django', "icdl"],
#     'summer': ['mcsa' , 'ccnp'],
#     'autumn': ['python' , 'photoshop' , 'C#'],
#     'winter': ['django2' , 'python' ' net +'],
# }

# list_butten = ['Back']

# user_info ={

# }

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
#     btn1 = types.KeyboardButton('Contact')
#     btn2 = types.KeyboardButton('Back')
#     btn3 = types.KeyboardButton('Call_number')
#     markup.add(btn1 , btn2 , btn3)
#     bot.reply_to(message , 'یکی از دکمه های زیر را انتخاب کنید' , reply_markup=markup)
#     bot.register_next_step_handler(message , btn)



    
# @bot.message_handler(commands=['Call_number'])
# def about(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
#     bot.reply_to(message , 'در صورت نیاز با شماره\n08612345\nتماس بگیرید')
#     for about in list_butten:
#         markup.add(types.KeyboardButton(about))
#     bot.reply_to(message ,'_', reply_markup=markup)

# def contact(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=4)
#     bot.reply_to(message , 'یکی از فصل های زیر را انتخاب کنید')
#     for contact in list_butten:
#         btn1 = types.KeyboardButton('spring')
#         btn2 = types.KeyboardButton('summer')
#         btn3 = types.KeyboardButton('autumn')
#         btn4 = types.KeyboardButton('winter')
#         btn5 = types.KeyboardButton('Back')
#     markup.add(btn1 , btn2 , btn3 , btn4 , btn5)
#     bot.reply_to(message ,'یک فصل', reply_markup=markup)
#     bot.register_next_step_handler(message , btn)


# def Spring(message):
#     markup = types.InlineKeyboardMarkup()
#     b1 = types.InlineKeyboardButton('ccna' , callback_data='ccna')
#     b2 = types.InlineKeyboardButton('lpic' , callback_data='btn1')
#     b3 = types.InlineKeyboardButton('net +' , callback_data='btn1')

#     markup.add(b1 , b2 , b3)
#     bot.reply_to(message , 'متن دلخواه' , reply_markup=markup)

# def Summer(message):
#     markup = types.InlineKeyboardMarkup()
#     a1 = types.InlineKeyboardButton('django' , callback_data='ccna')
#     a2 = types.InlineKeyboardButton('python' , callback_data='btn1')

#     markup.add(a1 , a2)
#     bot.reply_to(message , 'متن دلخواه' , reply_markup=markup)

# def Autumn(message):
#     markup = types.InlineKeyboardMarkup()
#     A1 = types.InlineKeyboardButton('django2' , callback_data='ccna')
#     A2 = types.InlineKeyboardButton('lpic' , callback_data='btn1')

#     markup.add(A1 , A2)
#     bot.reply_to(message , 'متن دلخواه' , reply_markup=markup)

# def Winter(message):
#     markup = types.InlineKeyboardMarkup()
#     w1 = types.InlineKeyboardButton('django2' , callback_data='ccna')
#     w2 = types.InlineKeyboardButton('lpic' , callback_data='btn1')

#     markup.add(w1 , w2)
#     bot.reply_to(message , 'متن دلخواه' , reply_markup=markup)


# @bot.callback_query_handler(func=lambda call:True)
# def Name(call):
#     message = call.message
#     bot.reply_to(message , 'نام خود را وارد کنید')
#     user_info['course'] = message
#     bot.register_next_step_handler(message , phone) 
# def phone(message):
#     bot.reply_to(message , 'شماره خود را وارد کنید')
#     user_info['name'] = message
#     bot.register_next_step_handler(message , finish)
# def finish(message):
#     bot.reply_to(message , 'ثبت نام شما انجام شد')
#     user_info['phone'] = message
#     with open("./info.txt" , "a") as file:
#         for key in user_info:
#             file.write(str(user_info[key]))



# @bot.message_handler(func=lambda message: True)
# def btn(message):
#     if message.text == 'Back':
#         start(message)
#     elif message.text == 'Contact':
#         contact(message)
#     elif message.text == 'Call_number':
#         about(message)
#     elif message.text == 'spring':
#         Spring(message)
#     elif (message.text == 'summer'):
#         Summer(message)
#     elif (message.text == 'autumn'):
#         Autumn(message)
#     elif (message.text == 'winter'):
#         Winter(message)




# bot.infinity_polling()




import telebot
import os
from telebot import types

API_TOKEN = os.environ.get('API_TOKENN')
bot = telebot.TeleBot(API_TOKEN)

user_info = {}

glass = {
    'spring': ['ccna', 'lpic', 'django', 'icdl'],
    'summer': ['mcsa', 'ccnp'],
    'autumn': ['python', 'photoshop', 'C#'],
    'winter': ['django2', 'python', 'net+'],
}

list_butten = ['Back']

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Contact')
    btn2 = types.KeyboardButton('Call_number')
    markup.add(btn1, btn2)
    bot.reply_to(message, 'یکی از دکمه های زیر را انتخاب کنید', reply_markup=markup)

@bot.message_handler(commands=['Call_number'])
def about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Back')
    markup.add(btn1)
    bot.reply_to(message, 'در صورت نیاز با شماره\n08612345\nتماس بگیرید', reply_markup=markup)

@bot.message_handler(commands=['Contact'])
def contact(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn1 = types.KeyboardButton('spring')
    btn2 = types.KeyboardButton('summer')
    btn3 = types.KeyboardButton('autumn')
    btn4 = types.KeyboardButton('winter')
    btn5 = types.KeyboardButton('Back')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.reply_to(message, 'یکی از فصل های زیر را انتخاب کنید', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def btn(message):
    if message.text == 'Back':
        start(message)
    elif message.text == 'Contact':
        contact(message)
    elif message.text == 'Call_number':
        about(message)
    elif message.text in glass:
        show_courses(message)

def show_courses(message):
    season = message.text.lower()
    courses = glass.get(season, [])
    markup = types.InlineKeyboardMarkup()
    for course in courses:
        markup.add(types.InlineKeyboardButton(course, callback_data=course))
    bot.reply_to(message, 'دوره ها:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    message = call.message
    bot.reply_to(message, 'نام خود را وارد کنید')
    user_info['course'] = call.data
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_info['name'] = message.text
    bot.reply_to(message, 'شماره خود را وارد کنید')
    bot.register_next_step_handler(message, get_phone)
# def get_name(message):
#     user_info['name'] = message.text
#     bot.reply_to(message, 'شماره خود را وارد کنید')
#     bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    phone_number = message.text
    if phone_number.isdigit():
        user_info["phone"]=phone_number
        bot.reply_to(message, 'پیش ثبت نام شما انجام شد👌')
        with open("./info.txt", "a") as file:
          for key in user_info:
            file.write(f"{key}: {user_info[key]}\n")
    else:
        bot.reply_to(message,"لطفا فقط عدد وارد کنید ")
        bot.register_next_step_handler(message,get_phone)
bot.infinity_polling()