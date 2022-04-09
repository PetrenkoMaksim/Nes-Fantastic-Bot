import telebot
import os

from bot_commands import bot_commands
from syllabus import syllabus_questions
API_KEY = "5163766250:AAFLX2d1oB2ddyRx_ihb5TrGoO_vnVuFMBY"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["start"])
def instructions(message):
    bot.send_message(message.chat.id, bot_commands["start"])

@bot.message_handler(commands=["syllabus"])
def instructions(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text="Course Description", callback_data="course description"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Grading policy", callback_data="Grading policy"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Deadline policy", callback_data="Deadline policy"))
    bot.send_message(message.chat.id, "These are the most frequently asked questions", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text in syllabus_questions.keys():
        bot.send_message(message.chat.id, syllabus_questions[message.text])

bot.polling()