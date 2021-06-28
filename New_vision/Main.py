from threading import Thread
import Main_GUI
import Stream_2
import logic_center



# th = Thread(target=logic_center.remote_control_install, daemon=True)
# th.start()
# th1 = Thread(target=Stream_2.start2, daemon=True)
# th1.start()
th = Thread(target=Stream_2.start1, daemon=True)
th.start()
th2 = Thread(target=Stream_2.parsing_ESP, daemon=True)
th2.start()
th3 = Thread(target=Stream_2.parsing_GPIO_Sadok, daemon=True)
th3.start()
th4 = Thread(target=Stream_2.parsing_GPIO_4relay11, daemon=True)
th4.start()

Main_GUI.root.mainloop()
