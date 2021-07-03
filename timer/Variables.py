import multiprocessing
import this
from multiprocessing import Process
from threading import Thread
from time import sleep
from tkinter import messagebox

import pygame
import pyglet

input_combo_box = 0
sound = False
file_name = ''
set_h = 0
set_m = 0
set_s = 0
set_timer_time = "00:00:00"
stop_timer = True

h = 0
m = 0
s = 0

music_play = ''
show_info = ''


def message():
    global music_play
    music_play = 'play'
    th1 = Thread(target=run_mp3_by_time_is_gone, daemon=True)
    th1.start()
    music_play = messagebox.showinfo('Python Timer by Stepa075', 'Таймер: время вышло!')

def run_mp3_by_time_is_gone():

    pygame.mixer.init()
    pygame.mixer.music.load("sirena.mp3")
    pygame.mixer.music.play()
    # song = pyglet.media.load('brigada.mp3')
    # song.play()
    # pyglet.app.run()
    # sleep(10.0)
    while True:
        if music_play == 'ok':
            # pyglet.app.exit()
            pygame.mixer.music.stop()
            print( 'while= ' + music_play)
        # elif show_info == 'play':
        #     pygame.mixer.music.play()
        # break
        sleep(1.0)

def run_mp3():

    pygame.mixer.init()
    pygame.mixer.music.load("brigada.mp3")
    pygame.mixer.music.play()
    # song = pyglet.media.load('brigada.mp3')
    # song.play()
    # pyglet.app.run()
    # sleep(10.0)
    while True:
        if show_info == 'ok':
            # pyglet.app.exit()
            pygame.mixer.music.stop()
            print( 'while= ' + show_info)
        # elif show_info == 'play':
        #     pygame.mixer.music.play()
        # break
        sleep(1.0)




def about():
    global show_info
    show_info = 'play'

    # proc = Process(target=run_mp3, name='run mp3')
    # proc.start()
    th = Thread(target=run_mp3, daemon=True)
    th.start()


    show_info = messagebox.showinfo('About: Python Timer by Stepa075',
                                    ' Данный таймер является дополнением к '
                                    ' программе Control Panel, но работает '
                                    ' и как самостоятельная программа.'
                                    ' © 2021 Программа написана мной, Stepa075,'
                                    ' чтобы пользовались все, кому это нужно.'
                                    ' Лицензия: GNU, General Public License (GPL)'
                                    ' Высылаем замечания на xmsa2014@gmail.com')

    # if show_info == 'ok':
    #     proc.terminate()
    print(show_info)
    # proc.terminate()
