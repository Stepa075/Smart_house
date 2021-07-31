import time



from New_vision.Mobile_app import Variables, main2


def start(self, event):
    while True:
        main2.MenuScreen.update(self, event)
        time.sleep(1.0)
def pumping():
   i = 0
   while i < 10:
       Variables.pomp_state = i
       i += 1
       print(str(Variables.pomp_state))

       time.sleep(1.0)


