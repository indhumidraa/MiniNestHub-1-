import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import mysql.connector


class corrector:
    def __init__(self, root):
        self.root = root
        self.root.title("Spell Corrector")
        self.root.geometry("400x200")



        def correction():
            input_word = word1_field.get()
            blob_obj = TextBlob(input_word)
            corrected_word = str(blob_obj.correct())
            word2_field.insert(10, corrected_word)

        def clear_all():
            word1_field.delete(0, tk.END)
            word2_field.delete(0, tk.END)

        # Spell Corrector UI
        tk.Label(root, text="Input Word").grid(row=0, column=0, padx=10, pady=10)
        word1_field = tk.Entry(root)
        word1_field.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Corrected Word").grid(row=1, column=0, padx=10, pady=10)
        word2_field = tk.Entry(root)
        word2_field.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(root, text="Correct", command=correction).grid(row=2, column=1, pady=10)
        tk.Button(root, text="Clear", command=clear_all).grid(row=3, column=1, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = corrector(root)
    root.mainloop()
