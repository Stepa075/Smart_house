from tkinter import *
from tkinter import ttk
def menu_btn_press(*event):
    t_password_fr.place_forget()
    t_settings_fr.place_forget()
    t_menu_gr.place(x = 270,y = 50)

def password_btn_press(*event):
    t_menu_gr.place_forget()
    t_settings_fr.place_forget()
    t_password_fr.place(x = 270,y = 50)

def settings_btn_press(*event):
    t_menu_gr.place_forget()
    t_password_fr.place_forget()
    t_settings_fr.place(x = 270,y = 50)

root = Tk()
root.title("Program")
root.geometry('1024x700')

main_fr = Frame(root,width=260,height=700, bg='#FFEFD5')
main_fr.place(x = 0,y = 0)

menu_fr= ttk.Frame(main_fr,width=200,height=40)
menu_fr.place(x = 20,y = 100)

password_fr = ttk.Frame(main_fr,width=200,height=40)
password_fr.place(x = 20,y = 150)

settings_fr = ttk.Frame(main_fr,width=200,height=40)
settings_fr.place(x = 20,y = 200)

menu_btn = Button(menu_fr, text="Меню",width=30,height=2, command=menu_btn_press, activebackground='#FF4500')
menu_btn.place(x=5, y=2)

password_btn = Button(password_fr, text="Пароли",width=30,height=2, command=password_btn_press, activebackground='#FF4500')
password_btn.place(x=5, y=2)

settings_btn = Button (settings_fr, text='Настройки',width=30,height=2, command=settings_btn_press, activebackground='#FF4500')
settings_btn.place(x=5, y=2)

t_password_fr = ttk.Frame(root, width=320,height=700)
ttk.Label(t_password_fr,text='Passwords:',font='arial 14').place(x = 200, y = 50)

t_menu_gr = ttk.Frame(root,width=320,height=700)
ttk.Label(t_menu_gr,text='Menu:       ',font='arial 14').place(x = 200, y = 50)

t_settings_fr = ttk.Frame(root,width=320,height=700)
ttk.Label(t_settings_fr,text='Settings:       ',font='arial 14').place(x = 200, y = 50)

root.mainloop()