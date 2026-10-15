import tkinter as tk
from tkinter import messagebox
import random

# List of words
words = ['indentation', 'comments', 'variables', 'output', 'print', 'string',
         'concatenation', 'int', 'float', 'complex', 'random', 'literals',
         'unicode', 'boolean', 'return', 'operators', 'lists', 'iterate',
         'tuple', 'loop', 'module', 'dictionary', 'nest', 'else', 'elif',
         'while', 'break', 'pass', 'function', 'arguments', 'keyword', 'parameter',
         'array', 'class', ' delete', 'import', 'convert', 'error', 'syntax']


# GUI part
hangmanpage = tk.Tk()

hangmanpage.geometry('500x500')
hangmanpage.resizable()
hangmanpage.title('Hangman')

label = tk.Label(hangmanpage, text="Guess the word:", font=("Helvetica", 16))
label.pack(pady=20)

entry = tk.Entry(hangmanpage, font=('Ink free', 20, 'bold'), bd=5)
entry.pack(pady=22)

button = tk.Button(hangmanpage, text="Check", font=('Ink free', 15, 'bold'), width=15, bg='#70c6dd', fg='white', activebackground='#70c6dd',
                   activeforeground='white', cursor='hand2', command=lambda: check())
button.pack()

lives_label = tk.Label(hangmanpage, text="Lives Remaining : 6", font=("Helvetica", 16))
lives_label.pack()

clue_label = tk.Label(hangmanpage, text="CLUE : Words are related to python", font=("Helvetica", 16))
clue_label.pack()


canvas = tk.Canvas(hangmanpage, width=300, height=400)
canvas.pack()

# Stand str
canvas.create_line(100, 100, 100, 300)
canvas.create_line(100, 100, 165, 100)
canvas.create_line(165, 100, 165, 150)

def draw_hangman(lives):
    if lives == 5:
        canvas.create_oval(175, 150, 150, 175)
    elif lives == 4:
        canvas.create_line(165, 175, 165, 240)
    elif lives == 3:
        canvas.create_line(165, 200, 140, 215)
    elif lives == 2:
        canvas.create_line(165, 200, 190, 215)
    elif lives == 1:
        canvas.create_line(165, 240, 140, 255)
    elif lives == 0:
        canvas.create_line(165, 240, 190, 255)


chosen_word = random.choice(words)
guessed_word = ["_"] * len(chosen_word)
lives = 6


def check():
    global lives
    guess = entry.get()
    entry.delete(0, 'end')

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        label.config(text=" ".join(guessed_word))

        if "".join(guessed_word) == chosen_word:
            messagebox.showinfo("You won!", "Congratulations, you guessed the word!")
    else:
        lives -= 1
        lives_label.config(text=f"Lives remaining: {lives}")
        draw_hangman(lives)

        if lives == 0:
            messagebox.showinfo("You lost", f"The word was {chosen_word}")


hangmanpage.mainloop()
