import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from tkinter import PhotoImage

# Database configuration
DB_CONFIG = {
    'user': 'root',
    'password': 'Gowri@123',
    'host': 'localhost',
    'database': 'user_db'
}


# GUI Setup
"""Create the main application window."""
signup_page = tk.Tk()
signup_page.title("Sign Up")

# Window configuration
signup_page.geometry("400x400")
signup_page.configure(bg="#f5f5f5")

# Frame for content
frame = tk.Frame(signup_page, bg="#ffffff")
frame.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)

# Title Label
title_label = tk.Label(frame, text="Sign Up", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333333")
title_label.pack(pady=10)



def create_db_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return None



def execute_query(query, data=None):
    global cursor
    connection = create_db_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
    except Error as e:
        messagebox.showerror("Database Error", f"Error executing query: {e}")
    finally:
        cursor.close()
        connection.close()

def validate_signup(username, password, confirm_password):
    """Validate sign-up input fields."""
    if not username or not password or not confirm_password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return False

    if password != confirm_password:
        messagebox.showwarning("Password Error", "Passwords do not match.")
        return False

    return True

def check_username_exists(username):
    """Check if the username already exists in the database."""
    connection = create_db_connection()
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result is not None
    except Error as e:
        messagebox.showerror("Database Error", f"Error checking username: {e}")
        return False
    finally:
        cursor.close()
        connection.close()

def handle_signup():
    """Handle the sign-up button click event."""
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not validate_signup(username, password, confirm_password):
        return

    if check_username_exists(username):
        messagebox.showwarning("User Exists", "Username already taken.")
        return

    try:
        execute_query(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        messagebox.showinfo("Success", "Sign-up successful!")
        signup_page.destroy()  # Close the sign-up window
        import login  # Show the login page
    except Error as e:
        messagebox.showerror("Error", f"Sign-up failed: {e}")




# Username
tk.Label(frame, text="Username", font=("Helvetica", 12), bg="#ffffff", fg="#333333").pack(anchor=tk.W, pady=5)
global entry_username
entry_username = tk.Entry(frame, font=("Helvetica", 12), bg="#e8e8e8", bd=0, relief="flat")
entry_username.pack(padx=10, pady=5, fill=tk.X)

# Password
tk.Label(frame, text="Password", font=("Helvetica", 12), bg="#ffffff", fg="#333333").pack(anchor=tk.W, pady=5)
global entry_password
entry_password = tk.Entry(frame, font=("Helvetica", 12), bg="#e8e8e8", bd=0, relief="flat", show="*")
entry_password.pack(padx=10, pady=5, fill=tk.X)

# Confirm Password
tk.Label(frame, text="Confirm Password", font=("Helvetica", 12), bg="#ffffff", fg="#333333").pack(anchor=tk.W,
                                                                                                      pady=5)
global entry_confirm_password
entry_confirm_password = tk.Entry(frame, font=("Helvetica", 12), bg="#e8e8e8", bd=0, relief="flat", show="*")
entry_confirm_password.pack(padx=10, pady=5, fill=tk.X)

# Sign-Up Button
sign_up_button = tk.Button(frame, text="Sign Up", font=("Helvetica", 14, "bold"), bg="#4caf50", fg="#ffffff",command=handle_signup)
sign_up_button.pack(pady=20, fill=tk.X)

# Run the application
signup_page.mainloop()


