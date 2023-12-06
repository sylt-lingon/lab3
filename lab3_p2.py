from tkinter import *
import random
from config import TITLE, WIDTH, HEIGHT, FONT, SYMBOLS


def get_key(x, start):
    s = start
    blok = start
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


def get_blok(a):
    return ''.join([random.choice(a) for i in range(5)])


def clicked():
    res = txt.get()
    key = get_key(res, get_blok(SYMBOLS))
    lbl_key = Label(window, text='Ваш ключ: ' + key, font=FONT)
    lbl_key.grid(column=1, row=3, padx=30, pady=0)


window = Tk()
window.title(TITLE)
window.geometry(f'{WIDTH}x{HEIGHT}')
bg_image = PhotoImage(file="fon.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text='Введите 3-значное число:', font=FONT)
lbl.grid(column=1, row=0, padx=30, pady=30)
txt = Entry(window, width=3, font=FONT)
txt.focus()
txt.grid(column=2, row=0, padx=0, pady=30)
btn = Button(window, text="Тык!", font=FONT, command=clicked)
btn.grid(column=3, row=0, padx=30, pady=30)

window.mainloop()
