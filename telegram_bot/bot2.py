import sys
from random import randint

import telebot

bot = telebot.TeleBot('1665828950:AAFIxWCJTvm1UyPNqRMdO-vsfs3HYAMxBUA')
count = 4  # количество цифр в загадываемом слове
ai = True  # если True то число генерируется самостоятельно, иначе вводится человеком
repetition = False  # указывает может ли повторятся цифра в загадываемом числе
number = list()


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")
    print('Print hello in chat!')


@bot.message_handler(commands=['game'])
def play(message):
    global number
    print("GO!")
    bot.send_message(message.from_user.id, text="Game started!")
    bot.send_message(message.from_user.id, "input count?")
    print()
    # if ai:
    number = list()

    for i in range(0, count):
        if not repetition:
            while True:
                e = str(randint(0, 9))
                if not e in number:
                    break
        else:
            e = str(randint(0, 9))
        number.append(e)

    bot.register_next_step_handler(message, game)


def game(message):
    # games = True
    # while games:
    print(number)

    # text1 = str(number)
    # text1 = update.message.text
    numb = str(message.html_text)
    if numb == 'exit':
        bot.send_message(message.from_user.id, text="Правильным числом было: ")
        bot.send_message(message.from_user.id, text=" ".join(str(x) for x in number))
        print("Правильным числом было ", number)
        start_command(message)
        return
    if len(numb) != len(number):
        bot.send_message(message.from_user.id, text="Количество цифр в вводимом числе не равно "
                                                    "количетсву цифр в загадываемом числе!")
        print("Количество цифр в вводимом числе не равно количетсву цифр в загадываемом числе!")

    cows = 0
    byki = 0
    for i in numb:
        try:
            if numb.index(i) == number.index(i):
                byki = byki + 1
            else:
                cows = cows + 1
        except ValueError:
            pass
    if byki == count:
        bot.send_message(message.from_user.id, text="Вы угадали число!!!")
        print("Вы угадали число!!!")
        bot.send_message(message.from_user.id, "Sigraem escho?")
        bot.register_next_step_handler(message, ask)

        return
    else:
        a = ("Коровы: {0}. Быки: {1}".format(cows, byki))
        bot.send_message(message.from_user.id, text=a)
        print("Коровы: {0}. Быки: {1}".format(cows, byki))
        bot.send_message(message.from_user.id, "input count?")
        bot.register_next_step_handler(message, game)


# bot.send_message(message.from_user.id, text="Быки-Коровы, Александр Гунгер 2019")
# bot.send_message(message.from_user.id, text="------Remastered by Stepa075------")

# print("Быки-Коровы, Александр Гунгер 2019")
# print("------Remastered by Stepa075------")
# print("Для выхода из программы нажмите Ctrl+C")
# while True:
#    bot.send_message(message.from_user.id, text="""      -     Для начала игры введите play
# -     Для выхода из программы введите exit
# """)
# #         word = input("""      -     Для начала игры введите play
# #       -     Для выхода из программы введите exit
# # """)
# word1 = str(text)
# if word1 == '/game':
#     # if True:
#     play()
# elif word == "exit":
#     exit(0)
# else:
#     print("ERROR: command by name '%s' not found. Please try again" % word)


# bot.send_message(message.from_user.id, text="Fuck!!!")
# bot.send_message(message.from_user.id, text="Пишите четырехзначные числа, с неповторяющимися цифрами!")
def ask(message):
    answer = message.text
    if str(answer) == 'Y':
        play(message)
    else:
        start_command(message)


@bot.message_handler(commands=['hi'])
def start_command_hi(message):
    bot.send_message(message.chat.id, "Hi!!! My dear friend!!!")


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, "Hi!!! I am a die!!!")
    quit(0)
    sys.exit(0)


bot.polling()
