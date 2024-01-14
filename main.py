from tkinter import *
from random import *

user_score = 0
computer_score =0

rock_text = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_text = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_text = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_names = [rock_text, paper_text, scissors_text]


def user_scorecard():
    global user_score
    user_score += 1
    user_score_label.config(text=f"User Score 👤:{user_score}")


def computer_scorecard():
    global computer_score
    computer_score += 1
    computer_score_label.config(text=f"Computer Score🖥:{computer_score}")


def winner(user_text, computer_text):
    if user_text == computer_text:
        winner_label.config(text="Match Draw🤝")
    elif user_text == rock_text and computer_text == paper_text:
        winner_label.config(text="Computer Won👎")
        computer_scorecard()
    elif user_text == scissors_text and computer_text == rock_text:
        winner_label.config(text="Computer Won👎")
        computer_scorecard()
    elif user_text == paper_text and computer_text == scissors_text:
        winner_label.config(text="Computer Won👎")
        computer_scorecard()
    else:
        winner_label.config(text="User Won!!🏆")
        user_scorecard()


def rock():
    user_label.config(text=rock_text)
    computer_choice = choice(list_names)
    computer_label.config(text=computer_choice)
    winner(rock_text, computer_choice)


def scissors():
    user_label.config(text=scissors_text)
    computer_choice = choice(list_names)
    computer_label.config(text=computer_choice)
    winner(scissors_text, computer_choice)


def paper():
    user_label.config(text=paper_text)
    computer_choice = choice(list_names)
    computer_label.config(text=computer_choice)
    winner(paper_text, computer_choice)


# Gui interface

window = Tk()
window.title("Rock-Paper-Scissors")
window.config(padx=50, pady=50, bg="#E9967A")

# Buttons

Rock_button = Button(text="Rock✊", width=31, font=("calibri", 12, "bold"), bg="#66CD00", command=rock)
Rock_button.grid(row=3, column=0, padx=20, pady=20)
scissors_button = Button(text="Scissors✌", width=31, font=("calibri", 12, "bold"), bg="#EE2C2C", command=scissors)
scissors_button.grid(row=3, column=2, padx=20, pady=20)
paper_button = Button(text="Paper✋", width=31, font=("calibri", 12, "bold"), bg="#00BFFF", command=paper)
paper_button.grid(row=3, column=1, padx=20, pady=20)

# Label

user_label = Label(text=rock_text, font=("calibri", 24, "bold"), bg="#E9967A")
user_label.grid(row=2, column=0)
computer_label = Label(text=rock_text, font=("calibri", 24, "bold"), bg="#E9967A")
computer_label.grid(row=2, column=2)
choose_label = Label(text="Rock ✊ - Paper ✋ - Scissors ✌ ", font=("calibri", 28, "bold"), bg="#E9967A")
choose_label.grid(row=0, column=0, columnspan=3, pady=30, padx=30)
user_score_label = Label(text="User Score 👤:0", font=("arial", 14, "bold"), bg="#E9967A")
user_score_label.grid(row=1, column=0)
computer_score_label = Label(text="Computer Score🖥:0", font=("arial", 14, "bold"), bg="#E9967A")
computer_score_label.grid(row=1, column=2)
winner_label = Label(text="", font=("calibri", 24, "bold"), bg="#E9967A")
winner_label.grid(row=2, column=1)

window.mainloop()
