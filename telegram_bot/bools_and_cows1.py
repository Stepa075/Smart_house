from random import randint

# global count, ai, repetition
count = 4  # количество цифр в загадываемом слове
ai = True  # если True то число генерируется самостоятельно, иначе вводится человеком
repetition = False  # указывает может ли повторятся цифра в загадываемом числе


def play():
    print("GO!")
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

    game = True
    while game:
        print(number)
        numb = list(input("Введите число: "))
        if numb == ['e', 'x', 'i', 't']:
            print("Правильным числом было ", number)
            return
        if len(numb) != len(number):
            print("Количество цифр в вводимом числе не равно количетсву цифр в загадываемом числе!")
            continue
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
            print("Вы угадали число!!!")
            return
        else:
            print("Коровы: {0}. Быки: {1}".format(cows, byki))


print("Быки-Коровы, Александр Гунгер 2019")
print("------Remastered by Stepa075------")
print("Для выхода из программы нажмите Ctrl+C")
while True:
    word = input("""      -     Для начала игры введите play
      -     Для выхода из программы введите exit
""")

    if word == "play":
        play()
    elif word == "exit":
        exit(0)
    else:
        print("ERROR: command by name '%s' not found. Please try again" % word)
