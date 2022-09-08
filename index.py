from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
from aiogram import types
from db import BotDB
import telebot;
from telebot import types
import config
BotDB.__init__(BotDB, 'safety.db')
bot = telebot.TeleBot('5650055557:AAGW0QAlGd7-lOM0RY97pfhwfaOEv9BC19E')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Greetings from Safety department of Venture Motor Freight LLC At first you need to sign up")
    bot.send_message(message.from_user.id, "Please enter your company name: ")
    bot.register_next_step_handler(message, get_company)

    
def get_company(message):
    global us_company
    us_company = message.text
    bot.send_message(message.from_user.id, "Please enter your name: ")
    bot.register_next_step_handler(message, get_name)
def get_name(message):
    global us_name
    us_name = message.text
    bot.send_message(message.from_user.id, "Please enter your surname: ")
    bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global us_surname
    us_surname = message.text
    bot.send_message(message.from_user.id, "Please enter your login: ")
    bot.register_next_step_handler(message, get_login)
def get_login(message):
    global us_login
    us_login = message.text
    bot.send_message(message.from_user.id, "Please enter your truck number: ")
    bot.register_next_step_handler(message, get_truck)
def get_truck(message):
    global us_truck
    us_truck = message.text
    bot.send_message(message.from_user.id, "Please enter your phone number: ")
    bot.register_next_step_handler(message, get_number)
def get_number(message):
    global us_number
    us_number = message.text
    bot.send_message(message.from_user.id, "Thank you You have been registered! Please choose /help ")
    BotDB.add_user(BotDB, us_login, us_name, us_surname, us_truck, us_number, us_company)



@bot.message_handler(commands=['help'])
def option (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Safety check")
    btn2 = types.KeyboardButton("Safety call me")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Sir, {0.first_name} please choose an option".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Safety check"):
        res = "Company: " + us_company + "\n" + "Driver name: " + us_name + "\n" + "Driver surname: " + us_surname + "\n" + "Driver's truck number: " + us_truck + "\n" + "Driver phone number: " + us_number + "\n " + "CHECK LOG BOOK"
        bot.send_message(chat_id =-1001303740156, text=res)
        bot.send_message(message.chat.id, text="We are checking It can take 10-30 min")
        
    elif(message.text == "Safety call me"):
        res = "Company: " + us_company + "\n" + "Driver name: " + us_name + "\n" + "Driver surname: " + us_surname + "\n" + "Driver's truck number: " + us_truck + "\n" + "Driver phone number: " + us_number + "\n " + "CALL TO DRIVER"
        bot.send_message(chat_id =-1001303740156, text=res)
        bot.send_message(message.chat.id, text="we will call you in some minutes Pls wait")
    else:
        bot.send_message(message.chat.id, text="Please choose one from options in button")
    
bot.polling(non_stop = True)
