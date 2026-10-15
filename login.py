import tkinter
from tkinter import *
from tkinter import messagebox  # Message box is inbuilt in tkinter
from tkinter import PhotoImage
import mysql.connector
from mysql.connector import Error


'''
Tk() -------->initialized tkinter which means window created
geometry() -->used when we want to set the width and height of the window
title() ----->used to give the title of the window
Label()------>widget use to display text that users can’t able to modify
mainpage -------->the name which we give to our window
pack() -------->organized widget in block
place() ----->used when we want to place widgets in a specific position
'''



# Database configuration
DB_CONFIG = {
    'user': 'root',
    'password': 'Gowri@123',
    'host': 'localhost',
    'database': 'user_db'
}

def create_db_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return None


# Defining a fn that is called when Login page is clicked
def signup():
    mainpage.destroy()
    import signup

def login():
    """Handle the login button click event."""
    username = usernameEntry.get()
    password = passwordEntry.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    connection = create_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            messagebox.showinfo("Success", "Login successful!")
            mainpage.destroy()
            import firstpage
        else:
            messagebox.showwarning("Login Error", "Invalid username or password.")
    except Error as e:
        messagebox.showerror("Database Error", f"Error during login: {e}")
    finally:
        cursor.close()
        connection.close()


mainpage = Tk()
mainpage.geometry('1280x700+0+0')
mainpage.resizable(False, False)
mainpage.title('MiniNestHub')

bimage = PhotoImage(file='bgimage.png')
bg_image = tkinter.Label(mainpage, image=bimage)
bg_image.place(relheight=1, relwidth=1)

#  Frame
loginFrame = Frame(mainpage, bg='#f0f4fe')
loginFrame.place(x=400, y=150)

# Label(logo)
logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame, image=logoImage, bg='#f0f4fe')
logoLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=20)
# columnspan takes 2 column spaces & pady and padx provides vertical and horizontal space


# Label(Username)
usernameimage = PhotoImage(file='username.png')
usernameLabel = Label(loginFrame, image=usernameimage, text='Username',
                      compound=LEFT, font=('Ink Free', 20, 'bold'), bg='#f0f4fe')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=('Ink free', 20, 'bold'), bd=5)
usernameEntry.grid(row=1, column=1)


# label(Password)
passwordimage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame, image=passwordimage, text='Password',
                      compound=LEFT, font=('Ink Free', 20, 'bold'), bg='#f0f4fe')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)
passwordEntry = Entry(loginFrame, font=('Ink free', 20, 'bold'), bd=5)
passwordEntry.grid(row=2, column=1)


# Button class
signinButton = Button(loginFrame, text='Sign in', font=('Ink free', 15, 'bold'), width=15,
                      bg='cornflowerblue', fg='white', activebackground='cornflowerblue',
                      activeforeground='white', cursor='hand2', command=login)
signinButton.grid(row=3, column=1, pady=10)


# Login label & signup button
displayLabel = Label(loginFrame, text="Don't have an account", font=('Ink Free', 20, 'bold'), bg='#f0f4fe')
displayLabel.grid(row=4, column=0)

signupButton = Button(loginFrame, text='Sign up', font=('Ink free', 15, 'bold'), width=15,  cursor='hand2', command=signup)
signupButton.grid(row=4, column=1)


# Label(Welcome)
welcome_label = tkinter.Label(mainpage, text='Welcome!', font=('Georgia', 30), bg='#e8eced')
welcome_label.pack()


mainpage.mainloop()