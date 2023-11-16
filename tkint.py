import tkinter
from tkinter import *
from PIL import Image, ImageTk


win = Tk()
win.title('Моя тестовая прога))')
win.geometry('500x400')

blok = IntVar()
cb1 = Checkbutton(text='есть брат/братья',bg='yellow', bd=1)
cb2 = Checkbutton(text='есть сестра/сестры')
cb1.place(relx=.5, rely=.5)
cb2.place(relx=.5, rely=.6)

rblok = IntVar()
rb1 = Radiobutton(text='есть только брат/братья',bg='yellow', value=1, variable=rblok)
rb2 = Radiobutton(text='есть только сестра/сестры', value=2, variable=rblok)
rb1.place(relx=.1, rely=.5)
rb2.place(relx=.1, rely=.6)

lst = ["Москва", "Сургут", "Омск", "Тюмень"]
lb = Listbox(bg='pink', height=4, width=15)
for i in lst:
    lb.insert(END, i)
lb.place(relx=.5, rely=.2, anchor='center')

def funk():
    tl = Toplevel()
    tl.geometry('300x100')
    text = Label(tl, text='Моя первая программа')
    text.place(relx=.5, rely=.5, anchor='center')

btn = Button(text='START', width=20, command=funk)
btn.place(relx=.5, rely=.8, anchor='center')


m_menu = Menu()
win.config(menu=m_menu)

filemenu = Menu(m_menu, tearoff=0)
filemenu.add_command(label='Открыть...')
filemenu.add_command(label='Новый')
filemenu.add_command(label='Сохранить...')
filemenu.add_command(label='Выход')
m_menu.add_cascade(label='Файл', menu=filemenu)

helpmenu = Menu(m_menu, tearoff=0)
helpmenu.add_command(label='Помощь')
helpmenu.add_command(label='О программе', command=funk)
m_menu.add_cascade(label='Справка', menu=helpmenu)




win.mainloop()
