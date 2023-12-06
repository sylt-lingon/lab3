from tkinter import *
from config import TITLE, WIDTH, HEIGHT, FONT


def next_page():
    window.destroy()
    import lab3_p2


window = Tk()
window.title(TITLE)
window.geometry(f'{WIDTH}x{HEIGHT}')
bg_image = PhotoImage(file="fon.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text='Сгенерировать ключ?', font=FONT)
lbl.grid(column=0, row=0, padx=50, pady=250)
btn = Button(window, text='Да!', font=FONT, command=next_page)
btn.grid(column=1, row=0, padx=10, pady=250)

window.mainloop()
