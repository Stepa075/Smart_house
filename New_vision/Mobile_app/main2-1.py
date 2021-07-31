import time

from kivy.app import App
from kivy.properties import Clock, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from New_vision.Mobile_app import Variables, logics


# class MySec(BoxLayout):
#
#     seconds_string = StringProperty('')    # Update time in GUI

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        # self.seconds_string = StringProperty('')
        self.button1 = Button(text='text')
        self.button2 = Button(text='World fgdhfghdsfghdhgdfghdf1', on_press = self.update)

        layout = GridLayout(cols=2, rows=5)
        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        # layout.add_widget(Button(text=str(MySec.seconds_string)))
        # layout.add_widget(Button(text='World 1'))
        # layout.add_widget(Button(text='Hello 2'))
        # layout.add_widget(Button(text='World 2'))
        # layout.add_widget(Button(text='Hello 1'))
        # layout.add_widget(Button(text='World 1'))
        # layout.add_widget(Button(text='Hello 2'))
        # layout.add_widget(Button(text='World 2'))
        # self.gr = GridLayout(cols=1, rows=4, spacing=10, size_hint_y=None)
        # self.gr.bind(minimum_height=self.gr.setter('height'))
        #
        # # inLayout = GridLayout(rows=3, size_hint=(0.2, 1))
        # self.gr.connects = Button( text='Связь с сервером', size_hint=(0.2, 1), background_color=(1, 0, 0, 1),)
        # self.gr.value = Button(text='Two', size_hint=(0.2, 1), on_press=lambda x: set_screen('add_food'))
        # self.gr.none = Button(text='Connect', size_hint=(0.2, 1), on_press=lambda x: set_screen('list_food'))
        # self.gr.none1 = Button(text='Reconnect', size_hint=(0.2, 1), on_press=lambda x: set_screen('list_food'))
        # self.connectsh = Button(background_color=(1, 0, 0, 1), text='Связь с умным домом')
        # self.value1 = Button(text='six', on_press=lambda x: set_screen('list_food'))
        # self.none2 = Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('add_food'))
        # self.none3 = Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food'))
        # self.control = Button(background_color=(1, 0, 0, 1), text='Управление')
        # self.value2 = Button(text='Two', on_press=lambda x: set_screen('add_food'))
        # self.controlr = Button(text='Удаленное', size_hint=(0.5, 1), on_press=lambda x: set_control('remote'))
        # self.controla = Button(text='Автомат', size_hint=(0.5, 1), on_press=lambda x: set_control('auto'))
        # self.power = Button(background_color=(1, 0, 0, 1), text='Питание в доме')
        # self.value3 = Button(text='Two', on_press=lambda x: set_screen('add_food'))
        # self.none4 = Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food'))
        # self.none6 = Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food'))
        # self.pump = Button(background_color=(1, 0, 0, 1), text='Положение насоса')
        # self.value4 = Button(text='', on_press=lambda x: set_screen('list_food'))
        # self.pumpon = Button(text='Включить', size_hint=(0.5, 1), on_press=lambda x: set_pump('on'))
        # self.pumpoff = Button(text='Выключить', size_hint=(0.5, 1), on_press=lambda x: set_pump('off'))

        self.add_widget(layout)
        # self.gr.add_widget(self.gr.connects)
        # self.gr.add_widget(self.gr.value)
        # self.add_widget(self.gr.none)
        # self.add_widget(self.gr.none1)
        # self.add_widget(self.connectsh)
        # self.add_widget(self.value1)
        # self.add_widget(self.none2)
        # self.add_widget(self.none3)
        # self.add_widget(self.control)
        # self.add_widget(self.value2)
        # self.add_widget(self.controlr)
        # self.add_widget(self.controla)
        # self.add_widget(self.power)
        # self.add_widget(self.value3)
        # self.add_widget(self.none4)
        # self.add_widget(self.none6)
        # self.add_widget(self.pump)
        # self.add_widget(self.value4)
        # self.add_widget(self.pumpon)
        # self.add_widget(self.pumpoff)




        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='Статус насоса'))
        # box.add_widget(Button(text='Two', on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='Датчик освещенности'))
        # box.add_widget(Button(text='six', on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='Реле садок'))
        # box.add_widget(Button(text='Two', on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='Включить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='Выключить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        #
        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='Реле тыл дома'))
        # box.add_widget(Button(text='Two', on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='Включить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='Выключить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='4 реле 1'))
        # box.add_widget(Button(text='six', on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='Включить', size_hint=(0.5, 1), on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='Выключить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='4 реле 2'))
        # box.add_widget(Button(text='Two', on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='Включить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='Выключить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='4 реле 3'))
        # box.add_widget(Button(text='six', on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='Включить', size_hint=(0.5, 1), on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='Выключить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(background_color=(1, 0, 0, 1), text='4 реле 4'))
        # box.add_widget(Button(text='six', on_press=lambda x: set_screen('list_food')))
        # box.add_widget(Button(text='Включить', size_hint=(0.5, 1), on_press=lambda x: set_screen('add_food')))
        # box.add_widget(Button(text='Выключить', size_hint=(0.5, 1), on_press=lambda x: set_screen('list_food')))

        # self.add_widget(box)

        # def update(self, event):
        #    global  but3
        #    while True:
        #     self.but3= str(Variables.pomp_state)
        #     time.sleep(1.0)
    def update(self, event):

              self.button1.text = str(Variables.pomp_state)
    def update1(self):

              self.button1.text = str(Variables.pomp_state)



class app1(App):


    def build(self):
        Clock.schedule_interval(lambda dt: self.update_time(), 1)  # Call update time
        Clock.schedule_interval(lambda dt: self.pr(), 1)
        
        return MenuScreen()

    def update_time(self):
            self.root.seconds_string = time.strftime("%S")  # Update time

    def pr(self):
            print(self.root.seconds_string)
            MenuScreen.update1(self)



            # Printing nime
            # x = int(self.root.seconds_string)  # String to integer
            # print(x * 2)  # Print result of integer operation


# class MySec(BoxLayout):
#
#     seconds_string = StringProperty('')    # Update time in GUI



# class MyApp(App):
#     def build(self):
#         Clock.schedule_interval(lambda dt: self.update_time(), 1)    #  Call update time
#         Clock.schedule_interval(lambda dt: self.pr(), 1)      #  Call printing time
#         return MySec()
#
#     def update_time(self):
#         self.root.seconds_string = time.strftime("%S")  #   Update time
#     def pr(self):
#         print(self.root.seconds_string)     #   Printing nime
#         # x=int(self.root.seconds_string)     #  String to integer
#         # print(x*2)                          # Print result of integer operation

if __name__ == '__main__':

    app1().run()


