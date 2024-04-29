import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('6540113782:AAHHoQq8246v3mMgoThe9jIr6uV8hPw5AVA')



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить водичку!')
    reminders_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminders_thread.start()


@bot.message_handler(commands=['fact'])
def fact(message):
    list = ['Водичка - самый вкусный продукт', 'Аномальное расширение воды при замерзании: В отличие от большинства веществ, вода расширяется и становится менее плотной, когда замерзает.',
            'Высокая теплоемкость: Вода имеет одну из самых высоких удельных теплоемкостей.', 'Вода как универсальный растворитель: Вода известна как «универсальный растворитель».']
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о воде: {random_fact}')

def send_reminders(chat_id):
    first_rem = "20:30"
    second_rem = "21:00"
    third_rem = "21:30"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == third_rem:
            bot.send_message(chat_id, f'Напоминание - выпей стакан воды!')
            time.sleep(62)
        time.sleep(1)



bot.polling(none_stop=True, interval=0)
