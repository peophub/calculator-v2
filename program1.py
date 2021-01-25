from tkinter import *
import math

window = Tk()
window.title("Калькулятор")
window.geometry('300x200')

def clicked_plus():
    val1 = txt_chislo.get()
    val2 = txt_chislo1.get()
    lbl_otvet.configure(text="Ответ: " + str(int(val1) + int(val2)))

def clicked_ymnozh():
    val1 = txt_chislo.get()
    val2 = txt_chislo1.get()
    lbl_otvet.configure(text="Ответ: " + str(int(val1) * int(val2)))

def clicked_delit():
    val1 = txt_chislo.get()
    val2 = txt_chislo1.get()
    lbl_otvet.configure(text="Ответ: " + str(int(val1) / int(val2)))

def clicked_koren():
    val1 = int(txt_chislo.get())
    lbl_otvet.configure(text="Ответ: " + str(math.sqrt(val1)))

def colored_fg():
    btn_plus.configure(fg=text_color.get())
    btn_color_bg.configure(fg=text_color.get())
    btn_color_fg.configure(fg=text_color.get())
    btn_ymnozh.configure(fg=text_color.get())
    btn_delit.configure(fg=text_color.get())
    btn_koren.configure(fg=text_color.get())

def colored_bg():
    btn_plus.configure(bg=text_color.get())
    btn_color_bg.configure(bg=text_color.get())
    btn_color_fg.configure(bg=text_color.get())
    btn_ymnozh.configure(bg=text_color.get())
    btn_delit.configure(bg=text_color.get())
    btn_koren.configure(bg=text_color.get())

text_color = Entry(window, width=10) #все про цвет
text_color.grid(column=0, row=0)
btn_color_fg = Button(window, text="Сменить цвет fg", command=colored_fg)
btn_color_fg.grid(column=1, row=0)
btn_color_bg = Button(window, text="Сменить цвет bg", command=colored_bg)
btn_color_bg.grid(column=2, row=0)

lbl_pusto = Label(window, text="    ") #заглушка
lbl_pusto.grid(column=0, row=1)

btn_plus = Button(window, text="сложить", command=clicked_plus) #все кнопки действий
btn_plus.grid(column=0, row=4)
btn_ymnozh = Button(window, text="умножить", command=clicked_ymnozh)
btn_ymnozh.grid(column=1, row=4)
btn_delit = Button(window, text="делить", command=clicked_delit)
btn_delit.grid(column=2, row=4)
btn_koren = Button(window, text="кв. корень", command=clicked_koren)
btn_koren.grid(column=0, row=5)

txt_chislo = Entry(window, width=5) #ввод чисел
txt_chislo.grid(column=0, row=3)
txt_chislo1 = Entry(window, width=5)
txt_chislo1.grid(column=1, row=3)

lbl_otvet = Label(window, text="Ответ:") #поле ответа
lbl_otvet.grid(column=0, row=2)

window.mainloop()