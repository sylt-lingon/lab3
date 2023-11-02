from tkinter import *
import random


def get_key(x):
    a = list('123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    blok = ''.join([random.choice(a) for i in range(5)])
    s = blok
    for i in range(3):
        blok = blok[:-1]
        k = int(str(x)[i])
        if i % 2 == 0:
            for j in range(k):
                blok += blok[0]
                blok = blok[1:]
        else:
            for j in range(k):
                blok = blok[-1] + blok
                blok = blok[:-1]
        s += '-' + blok
    return s


def clicked():
    res = txt.get()
    key = get_key(res)
    lbl_key = Label(window, text='Ваш ключ: ' + key, font=("Arial Bold", 20))
    lbl_key.grid(column=1, row=3, padx=30, pady=0)


window = Tk()
window.title('keygen')
window.geometry('800x600')
bg_image = PhotoImage(file="fon.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text='Введите 3-значное число:', font=("Arial Bold", 20))
lbl.grid(column=1, row=0, padx=30, pady=30)
txt = Entry(window, width=3, font=("Arial Bold", 20))
txt.focus()
txt.grid(column=2, row=0, padx=0, pady=30)
btn = Button(window, text="Тык!", font=("Arial Bold", 20), command=clicked)
btn.grid(column=3, row=0, padx=30, pady=30)

window.mainloop()
