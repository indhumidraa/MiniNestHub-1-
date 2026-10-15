import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gowri@123",
        database="todo_app"
    )


def add_task():
    task = task_entry.get()
    if not task:
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    cursor.close()
    conn.close()

    task_entry.delete(0, tk.END)
    load_tasks()


def load_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, status FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()

    tasks_list.delete(0, tk.END)
    for task in tasks:
        task_id, task_text, status = task
        display_text = f"{task_text} {'[Done]' if status else ''}"
        tasks_list.insert(tk.END, (task_id, display_text))


def mark_task_done():
    try:
        selected_task = tasks_list.get(tasks_list.curselection())
        task_id = selected_task[0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = TRUE WHERE id = %s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()

        load_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task!")


def delete_task():
    try:
        selected_task = tasks_list.get(tasks_list.curselection())
        task_id = selected_task[0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()

        load_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task!")

#  GUI
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.configure(bg="#f1e4e4")


task_entry = tk.Entry(root, width=30, font=("Arial", 14), bg="#f1e4e4")
task_entry.pack(pady=20)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#cb7589", fg="white", font=("Arial", 12), padx=10, pady=5)
add_button.pack(pady=10)


tasks_list = tk.Listbox(root, width=50, height=10, font=("Arial", 12), bg="#f1e4e4")
tasks_list.pack(pady=20)


mark_done_button = tk.Button(root, text="Mark as Done", command=mark_task_done, bg="#cb7589", fg="white", font=("Arial", 12), padx=10, pady=5)
mark_done_button.pack(pady=10)


delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#cb7589", fg="white", font=("Arial", 12), padx=10, pady=5)
delete_button.pack(pady=10)

# Initial task load
load_tasks()


root.mainloop()
