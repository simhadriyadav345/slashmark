import tkinter as tk
import random

def check_guess():
    guess = int(entry.get())
    
    if guess == number:
        result_label.config(text="Congratulations! You guessed it right!")
    elif guess < number:
        result_label.config(text="Too low! Try again.")
    else:
        result_label.config(text="Too high! Try again.")

def generate_number():
    global number
    number = random.randint(1, 100)

window = tk.Tk()
window.title("Number Guessing Game")

generate_number()

instruction_label = tk.Label(window, text="Guess a number between 1 and 100:")
instruction_label.pack()

entry = tk.Entry(window)
entry.pack()

check_button = tk.Button(window, text="Check", command=check_guess)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()