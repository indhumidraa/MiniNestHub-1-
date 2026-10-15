import tkinter as tk
from tkinter import messagebox


quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Venus", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Which ocean is the largest?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Southern Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain", "Leo Tolstoy"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["Gold", "Iron", "Diamond", "Platinum", "Quartz"],
        "answer": "Diamond"
    }
]


def check_answer(selected_choice):
    global current_question, score
    if selected_choice == quiz_data[current_question]["answer"]:
        score += 1

    current_question += 1
    if current_question < len(quiz_data):
        update_question()
    else:
        show_final_score()


def update_question():
    question_label.config(text=quiz_data[current_question]["question"])
    for i, choice in enumerate(quiz_data[current_question]["choices"]):
        buttons[i].config(text=choice, command=lambda c=choice: check_answer(c))


def show_final_score():
    messagebox.showinfo("Quiz Completed", f"You scored {score} out of {len(quiz_data)}")
    quizpage.quit()

# Setting up the GUI
quizpage = tk.Tk()
quizpage.title("General Knowledge Quiz Game")

current_question = 0
score = 0

question_label = tk.Label(quizpage, text=quiz_data[current_question]["question"], font=("Arial", 14))
question_label.pack(pady=20)

buttons = []
for i in range(5):
    btn = tk.Button(quizpage, text="", font=("Arial", 14))
    btn.pack(pady=5, fill=tk.X)
    buttons.append(btn)

update_question()

quizpage.mainloop()
