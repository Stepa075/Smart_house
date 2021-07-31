import time

import self
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_string("""
<MySec>:
    orientation: 'vertical'
    Label:
        id: kv_sec
        text: root.seconds_string
        font_size: 200
""")


class MySec(BoxLayout):

    seconds_string = StringProperty('')    # Update time in GUI



class MyApp(App):
    def build(self):
        Clock.schedule_interval(lambda dt: self.update_time(), 1)    #  Call update time
        Clock.schedule_interval(lambda dt: self.pr(), 1)      #  Call printing time
        return MySec()

    def update_time(self):
        self.root.seconds_string = time.strftime("%S")  #   Update time
    def pr(self):
        print(self.root.seconds_string)     #   Printing nime
        x=int(self.root.seconds_string)     #  String to integer
        print(x*2)                          # Print result of integer operation
if __name__ == '__main__':
    MyApp().run()