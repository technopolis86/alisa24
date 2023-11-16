from tkinter import *


x = 1
def focus():
    global x
    if x % 2 == 0:
        btn['text'] = '->'
        btn['bg'] = 'yellow'
        txt1.insert(0, txt2.get())
        txt2.delete(0, END)
    else:
        btn['text'] = '<-'
        btn['bg'] = 'red'
        txt2.insert(0, txt1.get())
        txt1.delete(0, END)

    x += 1

def math():
    txt4.insert(0, f'{eval(txt3.get()):.1f}')

s1 = 1
def show1():
    global s1
    print(s1)
    txt5 = Entry(win, width=20)
    txt5.place(relx=.4, rely=.46)
    if s1 % 2 == 0:
        txt5.lower()
        cb1['variable'] == 1
    else:

        txt5.lift()
        cb1['variable'] == 0
    s1 += 1


def show2():
    txt6.destroy()


win = Tk()
win.geometry('500x500')
win.resizable(width=False, height=False)
lb = Label(win, text='Эксперементы в tkinter', font=('Consolas', 20))
lb.place(relx=.5, rely=.05, anchor='c')

txt1 = Entry(win, width=20)
txt1.place(relx=.1, rely=.13)
txt1.insert(0, 'фокус')


btn = Button(text='->', width=2, height=2, bg='gold', command=focus)
btn.place(relx=.4, rely=.11)

txt2 = Entry(win, width=20)
txt2.place(relx=.5, rely=.13)

txt3 = Entry(win, width=20)
txt3.place(relx=.1, rely=.23)

btn1 = Button(text='!', width=2, height=2, bg='red', command=math)
btn1.place(relx=.4, rely=.21)

txt4 = Entry(win, width=20)
txt4.place(relx=.5, rely=.23)

cb1 = Checkbutton(width=5, height=5, variable=0, command=show1)
cb1.place(relx=.3, rely=.4)



cb2 = Checkbutton(width=5, height=5, command=show2)
cb2.place(relx=.3, rely=.5)
txt6 = Entry(win, width=20)
txt6.place(relx=.4, rely=.56)

cb3 = Checkbutton(width=5, height=5)
cb3.place(relx=.3, rely=.6)
txt7 = Entry(win, width=20)
txt7.place(relx=.4, rely=.66)

cb4 = Checkbutton(width=5, height=5)
cb4.place(relx=.3, rely=.7)
txt8 = Entry(win, width=20)
txt8.place(relx=.4, rely=.76)











def my_foo():
    print(456)





win.mainloop()

