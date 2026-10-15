import tkinter as tk
from tkinter import ttk

# Function to perform unit conversion
def unit_convertor():
    def convert_units():
        try:
            input_value = float(entry.get())
            from_unit = from_combobox.get()
            to_unit = to_combobox.get()
            category = category_combobox.get()

            conversions = {}
            converted_value = None

            if category == "Length":
                conversions = {
                    "meters": 1,
                    "kilometers": 0.001,
                    "feet": 3.28084,
                    "inches": 39.3701
                }
                converted_value = input_value * conversions[from_unit] / conversions[to_unit]
            elif category == "Weight":
                conversions = {
                    "grams": 1,
                    "kilograms": 0.001,
                    "pounds": 0.00220462,
                    "ounces": 0.035274
                }
                converted_value = input_value * conversions[from_unit] / conversions[to_unit]
            elif category == "Temperature":
                if from_unit == "Celsius" and to_unit == "Fahrenheit":
                    converted_value = (input_value * 9 / 5) + 32
                elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                    converted_value = (input_value - 32) * 5 / 9
                elif from_unit == "Celsius" and to_unit == "Kelvin":
                    converted_value = input_value + 273.15
                elif from_unit == "Kelvin" and to_unit == "Celsius":
                    converted_value = input_value - 273.15
                else:
                    converted_value = input_value  # Same unit conversion

            if converted_value is not None:
                result_label.config(text=f"Result: {converted_value:.2f} {to_unit}")
            else:
                result_label.config(text="Invalid conversion")

        except ValueError:
            result_label.config(text="Please enter a valid number.")

    # Clear the current frame
    for widget in pageFrame.winfo_children():
        widget.destroy()

    # Category selection
    category_label = tk.Label(pageFrame, text="Select Category:")
    category_label.place(x=800, y=100)

    category_combobox = ttk.Combobox(pageFrame, values=["Length", "Weight", "Temperature"])
    category_combobox.place(x=950, y=100)
    category_combobox.current(0)

    # Input value
    entry_label = tk.Label(pageFrame, text="Enter Value:")
    entry_label.place(x=800, y=140)

    entry = tk.Entry(pageFrame)
    entry.place(x=950, y=140)

    # From unit
    from_label = tk.Label(pageFrame, text="From:")
    from_label.place(x=800, y=180)

    from_combobox = ttk.Combobox(pageFrame, values=["meters", "kilometers", "feet", "inches"])
    from_combobox.place(x=950, y=180)
    from_combobox.current(0)

    # To unit
    to_label = tk.Label(pageFrame, text="To:")
    to_label.place(x=800, y=220)

    to_combobox = ttk.Combobox(pageFrame, values=["meters", "kilometers", "feet", "inches"])
    to_combobox.place(x=950, y=220)
    to_combobox.current(1)

    # Convert button
    convert_button = tk.Button(pageFrame, text="Convert", command=convert_units)
    convert_button.place(x=800, y=260)

    # Result label
    result_label = tk.Label(pageFrame, text="Result: ")
    result_label.place(x=950, y=260)

    # Update units based on category selection
    def update_units(event):
        if category_combobox.get() == "Length":
            from_combobox['values'] = ["meters", "kilometers", "feet", "inches"]
            to_combobox['values'] = ["meters", "kilometers", "feet", "inches"]
        elif category_combobox.get() == "Weight":
            from_combobox['values'] = ["grams", "kilograms", "pounds", "ounces"]
            to_combobox['values'] = ["grams", "kilograms", "pounds", "ounces"]
        elif category_combobox.get() == "Temperature":
            from_combobox['values'] = ["Celsius", "Fahrenheit", "Kelvin"]
            to_combobox['values'] = ["Celsius", "Fahrenheit", "Kelvin"]

        from_combobox.current(0)
        to_combobox.current(1)

    category_combobox.bind("<<ComboboxSelected>>", update_units)

# Function to perform currency conversion
def currency_convertor():
    def convert_currencies():
        try:
            input_value = float(entry.get())
            from_currency = from_combobox.get()
            to_currency = to_combobox.get()

            # Values taken at the time of program
            conversions = {
                "USD": 1,
                "EUR": 1.11,
                "GBP": 1.32,
                "JPY": 156.36,
                "IND": 83.96
            }

            if from_currency in conversions and to_currency in conversions:
                converted_value = input_value * conversions[to_currency] / conversions[from_currency]
                result_label.config(text=f"Result: {converted_value:.2f} {to_currency}")
            else:
                result_label.config(text="Invalid currency conversion.")

        except ValueError:
            result_label.config(text="Please enter a valid number.")

    # Clear the current frame
    for widget in pageFrame.winfo_children():
        widget.destroy()

    # Currency selection
    currency_label = tk.Label(pageFrame, text="Select Currency:")
    currency_label.place(x=800, y=100)

    currency_combobox = ttk.Combobox(pageFrame, values=["USD", "EUR", "GBP", "JPY","IND"])
    currency_combobox.place(x=950, y=100)
    currency_combobox.current(0)

    # Input value
    entry_label = tk.Label(pageFrame, text="Enter Amount:")
    entry_label.place(x=800, y=140)

    entry = tk.Entry(pageFrame)
    entry.place(x=950, y=140)

    # From currency
    from_label = tk.Label(pageFrame, text="From:")
    from_label.place(x=800, y=180)

    from_combobox = ttk.Combobox(pageFrame, values=["USD", "EUR", "GBP", "JPY","IND"])
    from_combobox.place(x=950, y=180)
    from_combobox.current(0)

    # To currency
    to_label = tk.Label(pageFrame, text="To:")
    to_label.place(x=800, y=220)

    to_combobox = ttk.Combobox(pageFrame, values=["USD", "EUR", "GBP", "JPY","IND"])
    to_combobox.place(x=950, y=220)
    to_combobox.current(1)

    # Convert button
    convert_button = tk.Button(pageFrame, text="Convert", command=convert_currencies)
    convert_button.place(x=800, y=260)

    # Result label
    result_label = tk.Label(pageFrame, text="Result: ")
    result_label.place(x=950, y=260)

    # Update currencies based on selection
    def update_currencies(event):
        currencies = ["USD", "EUR", "GBP", "JPY","IND"]
        from_combobox['values'] = currencies
        to_combobox['values'] = currencies
        from_combobox.current(0)
        to_combobox.current(1)

    currency_combobox.bind("<<ComboboxSelected>>", update_currencies)

# GUI setup
convpage = tk.Tk()
convpage.geometry('1280x700')
convpage.resizable(True, True)
convpage.title('Converter')
convpage.configure(bg='#ffebf7')

pageFrame = tk.Frame(convpage, bg='#ffebf7')
pageFrame.place(x=50, y=100, width=1180, height=500)

chooseLabel = tk.Label(convpage, text='Choose Converter:', font=('times new roman', 30, 'bold'), bg='#ffebf7')
chooseLabel.place(x=100, y=75)

# Unit Converter Button
unit_convertor_Button = tk.Button(convpage, text='Unit Converter', font=('Ink free', 15, 'bold'), width=20,
                                  fg='black', cursor='hand2', bg='#eccdd3', command=unit_convertor)
unit_convertor_Button.place(x=200, y=250)

# Currency Converter Button
currency_Button = tk.Button(convpage, text='Currency Converter', font=('Ink free', 15, 'bold'), width=20,
                             fg='black', cursor='hand2', bg='#eccdd3', command=currency_convertor)
currency_Button.place(x=200, y=450)

convpage.mainloop()
