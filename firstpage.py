import tkinter as tk
import time
from tkinter import PhotoImage, messagebox

def clock():
    currentdate = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M')
    datetimeLabel.config(text=f'        Date: {currentdate}\nTime: {currenttime}')

def rcs():
    firstpage.destroy()
    try:
        import rcs
    except ImportError as e:
        print(f"Failed to import rcs module: {e}")
        messagebox.showerror("Import Error", "Failed to import rcs module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the rcs module.")

def hangman():
    firstpage.destroy()
    try:
        import hangman
    except ImportError as e:
        print(f"Failed to import hangman module: {e}")
        messagebox.showerror("Import Error", "Failed to import hangman module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the hangman module.")

def quiz():
    firstpage.destroy()
    try:
        import quiz
        print("Quiz module imported successfully")
    except ImportError as e:
        print(f"Failed to import quiz module: {e}")
        messagebox.showerror("Import Error", "Failed to import quiz module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the quiz module.")

def mdlib():
    firstpage.destroy()
    try:
        import Madlib
        print("Madlib module imported successfully")
    except ImportError as e:
        print(f"Failed to import Madlib module: {e}")
        messagebox.showerror("Import Error", "Failed to import Madlib module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the Madlib module.")


def notes():
    firstpage.destroy()
    try:
        import Notes
        root = tk.Tk()
        app = Notes.Notes(root)
        root.mainloop()
        print("clock module imported successfully")
    except ImportError as e:
        print(f"Failed to import clock module: {e}")
        messagebox.showerror("Import Error", "Failed to import clock module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the clock module.")

def todolist():
    firstpage.destroy()
    try:
        import todolist
        print("Todolist module imported successfully")
    except ImportError as e:
        print(f"Failed to import todolist module: {e}")
        messagebox.showerror("Import Error", "Failed to import todolist module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the todolist module.")

def pomodoro():
    firstpage.destroy()
    try:
        import pomodoro
        print("Pomodoro module imported successfully")
    except ImportError as e:
        print(f"Failed to import pomodoro module: {e}")
        messagebox.showerror("Import Error", "Failed to import pomodoro module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the pomodoro module.")

def timer():
    firstpage.destroy()
    try:
        import Timer
        print("Timer module imported successfully")
    except ImportError as e:
        print(f"Failed to import timer module: {e}")
        messagebox.showerror("Import Error", "Failed to import timer module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the timer module.")

def corrector():
    firstpage.destroy()
    try:
        import corrector
        root = tk.Tk()
        app = corrector.corrector(root)
        root.mainloop()
        print("more module imported successfully")
    except ImportError as e:
        print(f"Failed to import more module: {e}")
        messagebox.showerror("Import Error", "Failed to import more module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the more module.")


def calculator():
    firstpage.destroy()
    try:
        import Calculator
        print("Calculator module imported successfully")
    except ImportError as e:
        print(f"Failed to import calculator module: {e}")
        messagebox.showerror("Import Error", "Failed to import calculator module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the calculator module.")


def bmi():
    firstpage.destroy()
    try:
        import BMI
        print(" BMI module imported successfully")
    except ImportError as e:
        print(f"Failed to import BMI module: {e}")
        messagebox.showerror("Import Error", "Failed to import BMI module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the BMI module.")

def convertor():
    firstpage.destroy()
    try:
        import Convertor
        print("Convertor module imported successfully")
    except ImportError as e:
        print(f"Failed to import Convertor module: {e}")
        messagebox.showerror("Import Error", "Failed to import Convertor module.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred while loading the Convertor module.")


# GUI part
firstpage = tk.Tk()
firstpage.geometry('1280x700+0+0')
firstpage.resizable()
firstpage.title('MiniNestHub')

bimage = PhotoImage(file='bgimage2.png')
bg_image = tk.Label(firstpage, image=bimage)
bg_image.place(relheight=1, relwidth=1)

# Frame
pageFrame = tk.Frame(firstpage, bg='#f0f4fe')
pageFrame.place(x=400, y=150)

# Date & time
datetimeLabel = tk.Label(firstpage, font=('times new roman', 20, 'bold'))
datetimeLabel.place(x=10, y=20)
clock()

# Heading label
chooseLabel = tk.Label(firstpage, text='Master your Mission', font=('times new roman', 30, 'bold'), bg='#f0dde1')
chooseLabel.place(x=500, y=20)


gameLabel = tk.Label(firstpage, text='Games', font=('Comic Sans MS', 30, 'bold'), bg='#f0eced')
gameLabel.place(x=100, y=150)


creativecornerLabel = tk.Label(firstpage, text='Creative Corner', font=('Comic Sans MS', 30, 'bold'), bg='#ecd6d9')
creativecornerLabel.place(x=500, y=150)

toolsLabel = tk.Label(firstpage, text='Basic Tools', font=('Comic Sans MS', 30, 'bold'), bg='#f2f0f1')
toolsLabel.place(x=1000, y=150)

# Games - Rock,Paper,Scissor
rcsButton = tk.Button(firstpage, text='Rock,Paper,Scissor', font=('Ink free', 15, 'bold'), width=15,
                   fg='black', cursor='hand2', command=rcs)
rcsButton.place(x=90, y=250)

# Games - Hangman
hangmanButton = tk.Button(firstpage, text='Hangman', font=('Ink free', 15, 'bold'), width=15,
                       fg='black', cursor='hand2', command=hangman)
hangmanButton.place(x=90, y=350)

# Games - Quiz
tbaButton = tk.Button(firstpage, text='Quiz', font=('Ink free', 15, 'bold'), width=15,
                   fg='black', cursor='hand2', command=quiz)
tbaButton.place(x=80, y=450)

# Games - Madlib
madlibButton = tk.Button(firstpage, text='Madlib', font=('Ink free', 15, 'bold'), width=15,
                      fg='black', cursor='hand2', command=mdlib)
madlibButton.place(x=80, y=550)

# Creative corner - Notes
clock_Button = tk.Button(firstpage, text='Notes', font=('Ink free', 15, 'bold'), width=15,
                      fg='black', cursor='hand2', bg='#eccdd3', command=notes)
clock_Button.place(x=550, y=250)

# Creative corner - Todolist
todolist_Button = tk.Button(firstpage, text='Todo-List', font=('Ink free', 15, 'bold'), width=15,
                      fg='black', cursor='hand2', bg='#eccdd3', command=todolist)
todolist_Button.place(x=550, y=350)

# Creative corner - pomodoro
pomodoro_Button = tk.Button(firstpage, text='Pomodoro', font=('Ink free', 15, 'bold'), width=15,
                      fg='black', cursor='hand2', bg='#eccdd3', command=pomodoro)
pomodoro_Button.place(x=550, y=450)

# Creative corner - Spell Corrector
more_Button = tk.Button(firstpage, text='Spell Corrector', font=('Ink free', 15, 'bold'), width=15,
                      fg='black', cursor='hand2', bg='#eccdd3', command=corrector)
more_Button.place(x=550, y=550)

# Tools - Timer
convertor_Button = tk.Button(firstpage, text='Timer', font=('Ink free', 15, 'bold'), width=15,
                      fg='black', cursor='hand2', bg='#eccdd3', command=timer)
convertor_Button.place(x=1000, y=250)

# Tools - Calculator
calculator_Button = tk.Button(firstpage, text='Calculator', font=('Ink free', 15, 'bold'), width=15,
                      fg='black', cursor='hand2', bg='#eccdd3', command=calculator)
calculator_Button.place(x=1000, y=350)

# Tools - BMI
bmiButton = tk.Button(firstpage, text='BMI Calculator', font=('Ink free', 15, 'bold'), width=20,
                   fg='black', cursor='hand2', bg='#eccdd3',command=bmi)
bmiButton.place(x=975, y=450)

# Tools - Convertor
convertor_Button = tk.Button(firstpage, text='Convertor', font=('Ink free', 15, 'bold'), width=20,
                   fg='black', cursor='hand2', bg='#eccdd3',command=convertor)
convertor_Button.place(x=975, y=550)



firstpage.mainloop()
