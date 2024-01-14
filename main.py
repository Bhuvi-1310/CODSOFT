from tkinter import *
from random import choice, shuffle


# PASSWORD GENERATOR

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(25)]
    if symbol_checkbox():
        password_symbols = [choice(symbols) for i in range(25)]
    else:
        password_symbols = []
    if number_checkbox():
        password_numbers = [choice(numbers) for i in range(25)]
    else:
        password_numbers = []

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    final_password = [choice(password_list) for i in range(length_spinbox())]

    password = "".join(final_password)
    password_entry.insert(0, password)


def length_spinbox():
    return int(len_spinbox.get())


def character_checkbox():
    return int(characters_state.get())


def number_checkbox():
    return int(numbers_state.get())


def symbol_checkbox():
    return int(symbols_state.get())


# UI SETUP

window = Tk()
window.geometry("580x280")
window.title("Password Generator")
window.config(padx=20, pady=20)

# Labels
password_generator_label = Label(text="Password Generator🔒", font=("calibri", 24, "bold"), width=31)
password_generator_label.grid(row=0, column=0, columnspan=3)
password_length_label = Label(text="Length Of Password:", width=31, font=("calibri", 10, "bold"))
password_length_label.grid(row=2, column=0)
password_setting_label = Label(text="Password Settings:", width=31, font=("calibri", 10, "bold"))
password_setting_label.grid(row=3, column=0)

# Spinbox
len_spinbox = Spinbox(from_=8, to=25, width=8, command=length_spinbox)
len_spinbox.grid(row=2, column=1)

# Checkbox
characters_state = IntVar()
character_checkbutton = Checkbutton(text="Characters🔡", variable=characters_state, width=8,
                                    font=("calibri", 10, "bold"), borderwidth=5)
characters_state.set(1)
character_checkbutton.grid(row=4, column=0)
numbers_state = IntVar()
number_checkbutton = Checkbutton(text="Numbers🔢", variable=numbers_state, width=31, font=("calibri", 10, "bold"))
number_checkbutton.grid(row=4, column=1)
symbols_state = IntVar()
symbol_checkbutton = Checkbutton(text="Symbols🔣", variable=symbols_state, width=31, font=("calibri", 10, "bold"))
symbol_checkbutton.grid(row=5, column=0)

# Entries
password_entry = Entry(width=31)
password_entry.grid(row=1, column=0, columnspan=3)

# Buttons
generate_password_button = Button(text="Generate Password▶", command=generate_password, width=31, bg="#00CD00",
                                  font=("calibri", 10, "bold"))
generate_password_button.grid(row=6, column=0, columnspan=3)

window.mainloop()
