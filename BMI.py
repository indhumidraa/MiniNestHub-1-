import tkinter as tk
from tkinter import messagebox

class BMI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.resizable()
        self.root.title("BMI Calculator")

        self.label = tk.Label(self.root, text="BMI Calculator", font=('Comic Sans MS', 20, 'bold'), bg='#f2f0f1')
        self.label.place(x=175,y=25)

        # Creating labels and entry fields for age, height, and weight
        self.label_age = tk.Label(self.root, text="Age:")
        self.label_age.place(x=200, y=100)
        self.entry_age = tk.Entry(self.root)
        self.entry_age.place(x=200, y=125)

        self.label_height = tk.Label(self.root, text="Height (cm):")
        self.label_height.place(x=200, y=200)
        self.entry_height = tk.Entry(self.root)
        self.entry_height.place(x=200, y=225)

        self.label_weight = tk.Label(self.root, text="Weight (kg):")
        self.label_weight.place(x=200, y=300)
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.place(x=200, y=325)

        self.button = tk.Button(self.root, text="Calculate", font=('Comic Sans MS', 20, 'bold'), bg='#f2f0f1', command=self.calculate_bmi)
        self.button.place(x=200, y=400)

    def calculate_bmi(self):
        try:
            weight = self.weight_var.get()
            height_cm = self.height_var.get()
            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)

            # Determine the BMI category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"

            result = f"BMI: {bmi:.2f}\nCategory: {category}"
            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")


    def calculate_bmi(self):
        age = int(self.entry_age.get())
        height = int(self.entry_height.get())
        weight = int(self.entry_weight.get())

        # Calculate BMI
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)

        # Display BMI category
        if bmi <= 16:
            messagebox.showinfo("BMI Category", "Severe Thinness")
        elif 16 < bmi <= 17:
            messagebox.showinfo("BMI Category", "Mild Thinness")
        elif 17 < bmi <= 18.5:
            messagebox.showinfo("BMI Category", "Moderate Thinness")
        elif 18.5 < bmi <= 25:
            messagebox.showinfo("BMI Category", "Normal")
        elif 25 < bmi <= 30:
            messagebox.showinfo("BMI Category", "Overweight")
        elif 30 <= bmi <= 35:
            messagebox.showinfo("BMI Category", "Obese Class I")
        elif 35 <= bmi <= 40:
            messagebox.showinfo("BMI Category", "Obese Class II")
        elif bmi > 40:
            messagebox.showinfo("BMI Category", "Obese Class III")

    def run(self):
        self.root.mainloop()

game = BMI()
game.run()