from tkinter import *


def next_page():
    window.destroy()
    import lab3_p2


window = Tk()
window.title('keygen')
window.geometry('800x600')
bg_image = PhotoImage(file="fon.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text='Сгенерировать ключ?', font=("Arial Bold", 30))
lbl.grid(column=0, row=0, padx=50, pady=250)
btn = Button(window, text='Да!', font=("Arial Bold", 25), command=next_page)
btn.grid(column=1, row=0, padx=10, pady=250)

window.mainloop()
