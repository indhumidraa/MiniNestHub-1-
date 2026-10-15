import tkinter as tk
from tkinter import PhotoImage
import time

# Timer settings (in seconds)
WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60

# Initialize the root window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("500x600")
root.config(bg="#f0f0f0")

# Initialize global variables
reps = 0
timer = None

# Timer reset function
def reset_timer():
    global reps
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg="#333333")
    reps = 0

# Timer start function
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK)
        timer_label.config(text="Long Break", fg="#e7305b")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK)
        timer_label.config(text="Short Break", fg="#e2979c")
    else:
        count_down(WORK_TIME)
        timer_label.config(text="Work", fg="#9bdeac")

# Countdown mechanism
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()

# UI setup
canvas = tk.Canvas(root, width=300, height=300, bg="#f0f0f0", highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=image)
timer_text = canvas.create_text(150, 180, text="00:00", fill="black", font=("Courier", 35, "bold"))
canvas.pack(pady=20)

timer_label = tk.Label(root, text="Timer", font=("Courier", 35, "bold"), bg="#f0f0f0", fg="#333333")
timer_label.pack(pady=10)

start_button = tk.Button(root, text="Start", command=start_timer, bg="#9bdeac", font=("Courier", 12, "bold"), pady=5, padx=20)
start_button.pack(side="left", padx=20, pady=20)

reset_button = tk.Button(root, text="Reset", command=reset_timer, bg="#e7305b", font=("Courier", 12, "bold"), pady=5, padx=20)
reset_button.pack(side="right", padx=20, pady=20)

# Start the application
root.mainloop()
