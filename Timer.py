import time
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("300x250")
root.title("Time Counter")

# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")


hourEntry = Entry(root, width=3, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=180, y=20)


def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:

        print("Please input the right value")

    while temp > -1:


        mins, secs = divmod(temp, 60)   # divmod (firstvalue = temp//60, secondvalue = temp%60)

        # Converting the input entered in mins or secs to hours,
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up ")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# button widget
btn = Button(root, text="Let's start", bd='5',
             command=submit)
btn.place(x=70, y=120)

root.mainloop()