import tkinter
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
import random

rcspage = Tk()
rcspage.geometry("1280x700+0+0")
rcspage.title("Rock Paper Scissor Game")


# Adding the images
rock = PhotoImage(file='Rock.png')
paper = PhotoImage(file='Paper.png')
scissor = PhotoImage(file='Scissors.png')


# Adding the images to a list
image_list = [rock, paper, scissor]

# Pick a random number bw 0 & 2
picknum = random.randint(0, 2)

# Image & Welcome when program starts

image_start = PhotoImage(file='Rock Paper Scissors.png')
WelcomeLabel = Label(rcspage, text='Welcome!!!', font=('Ink Free', 30, 'bold'))
WelcomeLabel.place(x=700, y=100)
image_startLabel = Label(rcspage, image=image_start)
image_startLabel.place(x=400, y=0)


# Comp image & Comp text
compLabel = Label(rcspage, text='Computer:', font=('Ink Free', 30, 'bold'))
compLabel.place(x=0, y=300)
imageLabel = Label(rcspage, image=image_list[picknum], bg='#f1f1e9')
imageLabel.place(x=0, y=400)


# Create spin function
def spin():
    global picknum
    # Showing image
    imageLabel.config(image=image_list[picknum])

    # 0 ==> Rock
    # 1 ==> Paper
    # 2 ==> Scissors

    # Converting dropdown choice to num
    if user_choice.get() == 'Rock':
        user_choice_value = 0
    elif user_choice.get() == 'Paper':
        user_choice_value = 1
    elif user_choice.get() == 'Scissors':
        user_choice_value = 2

    # Determining win or loss
    if user_choice_value == 0:  # Rock
        if picknum == 0:  # Rock
            winlooseLabel.config(text="It's A TIE! Spin Again...")
        elif picknum == 1:  # Paper
            winlooseLabel.config(text="Paper Covers Rock! You loose")
        elif picknum == 2:  # Scissors
            winlooseLabel.config(text="Rock smashes Scissors! You Win")


    elif user_choice_value == 1:  # Paper
        if picknum == 0:  # Rock
            winlooseLabel.config(text="Paper Covers Rock! You Win")
        elif picknum == 1:  # Paper
            winlooseLabel.config(text="It's A TIE! Spin Again...")
        elif picknum == 2:  # Scissors
            winlooseLabel.config(text="Scissors cut Paper! You Loose")


    elif user_choice_value == 2:  # Scissors
        if picknum == 0:  # Rock
            winlooseLabel.config(text="Rock smashes Scissors! You Loose")
        elif picknum == 1:  # Paper
            winlooseLabel.config(text="Scissors cut Paper! You Win")
        elif picknum == 2:  # Scissors
            winlooseLabel.config(text="It's A TIE! Spin Again...")


# You message
compLabel = Label(rcspage, text='You:', font=('Ink Free', 30, 'bold'))
compLabel.place(x=1000, y=300)


# User input
user_choice = ttk.Combobox(rcspage, values=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.place(x=1000, y=400)


# Create spin button
spinButton = Button(rcspage, text='Spin!', font=('Ink Free', 30, 'bold'), command=spin)
spinButton.place(x=600, y=500)

# Showing win or loose message
winlooseLabel = Label(rcspage, text="", font=('Ink Free', 20, 'bold'))
winlooseLabel.place(x=450, y=350)


rcspage.mainloop()
