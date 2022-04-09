import telebot
import os

from bot_commands import bot_commands
from syllabus import syllabus_questions
from syllabus_pictures import syllabus_pictures
API_KEY = "5163766250:AAFLX2d1oB2ddyRx_ihb5TrGoO_vnVuFMBY"
bot = telebot.TeleBot(API_KEY)

commands_list = ["start", "instructions"]
@bot.message_handler(commands=[command for command in commands_list])
def instructions(message):
    bot.send_message(message.chat.id, bot_commands[message.text[1:]])

@bot.message_handler(commands=["syllabus"])
def instructions(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    SyllabusKeybordButtons = ["Syllabus", "Course description",
                              "Grading policy", "Deadline policy",
                              "Make-up policy", "Weekly Reading Journals",
                              "Final Project"]
    for button in SyllabusKeybordButtons:
        keyboard.add(telebot.types.InlineKeyboardButton(text=button, callback_data=button))
    bot.send_message(message.chat.id, "These are the most frequently asked questions.", reply_markup=keyboard)

# syllabus replies

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text in syllabus_pictures.keys():
        photo = open(syllabus_pictures[message.text], "rb")
        bot.send_photo(message.chat.id, photo)

    elif message.text in syllabus_questions.keys():
        bot.send_message(message.chat.id, syllabus_questions[message.text])


bot.polling()