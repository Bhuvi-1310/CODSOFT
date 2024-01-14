from tkinter import *


def button_text(num):
    global entry_text
    entry_text = entry_text + str(num)
    entry_label.set(entry_text)


def equals():
    global entry_text
    try:
        total = str(eval(entry_text))
        entry_label.set(total)
        entry_text = total

    except SyntaxError:
        entry_label.set("syntax error")
        entry_text = ""

    except ZeroDivisionError:
        entry_label.set("Can't divide by zero")
        entry_text = ""


def clear():
    global entry_text
    entry_label.set("")
    entry_text = ""


window = Tk()
window.title("Calculator program")
window.geometry("600x600")

entry_text = ""

entry_label = StringVar()

label = Label(window, textvariable=entry_label, font=('calibri', 20), bg="white", width=24, height=2)
label.pack()

proj_frame = Frame(window)
proj_frame.pack()

#--------Buttons---------#

button1 = Button(proj_frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_text(1))
button1.grid(row=0, column=0)

button2 = Button(proj_frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_text(2))
button2.grid(row=0, column=1)

button3 = Button(proj_frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_text(3))
button3.grid(row=0, column=2)

button4 = Button(proj_frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_text(4))
button4.grid(row=1, column=0)

button5 = Button(proj_frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_text(5))
button5.grid(row=1, column=1)

button6 = Button(proj_frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_text(6))
button6.grid(row=1, column=2)

button7 = Button(proj_frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_text(7))
button7.grid(row=2, column=0)

button8 = Button(proj_frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_text(8))
button8.grid(row=2, column=1)

button9 = Button(proj_frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_text(9))
button9.grid(row=2, column=2)

button0 = Button(proj_frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_text(0))
button0.grid(row=3, column=0)

plus = Button(proj_frame, text='+', height=4, width=9, font=35,
              command=lambda: button_text('+'))
plus.grid(row=3, column=2)

minus = Button(proj_frame, text='-', height=4, width=9, font=35,
               command=lambda: button_text('-'))
minus.grid(row=2, column=3)

multiply = Button(proj_frame, text='*', height=4, width=9, font=35,
                  command=lambda: button_text('*'))
multiply.grid(row=1, column=3)

divide = Button(proj_frame, text='/', height=4, width=9, font=35,
                command=lambda: button_text('/'))
divide.grid(row=0, column=3)

equal = Button(proj_frame, text='=', height=4, width=9, font=35,
               command=equals)
equal.grid(row=3, column=3)

modulo = Button(proj_frame, text='%', height=4, width=9, font=35,
                command=lambda:button_text('%'))
modulo.grid(row=1, column=4)

decimal = Button(proj_frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_text('.'))
decimal.grid(row=3, column=1)

clear = Button(proj_frame, text='AC', height=4, width=9, font=35,
               command=clear)
clear.grid(row=0,column=4)

window.mainloop()
