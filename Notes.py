import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector

class Notes:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("600x600")


        # Connect to MySQL Database
        try:
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Gowri@123",
                database="notes_db"
            )
            db_cursor = db_connection.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return


        def add_note():
            title = title_entry.get()
            content = content_text.get("1.0", tk.END).strip()

            if not title or not content:
                messagebox.showwarning("Input Error", "Title and content cannot be empty!")
                return

            try:
                query = "INSERT INTO notes (title, content) VALUES (%s, %s)"
                db_cursor.execute(query, (title, content))
                db_connection.commit()
                messagebox.showinfo("Success", "Note added successfully!")
                clear_fields()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

        def view_notes():
            notes_list.delete(0, tk.END)
            db_cursor.execute("SELECT id, title FROM notes")
            for note in db_cursor.fetchall():
                notes_list.insert(tk.END, f"{note[0]}: {note[1]}")

        def edit_note():
            selected = notes_list.get(tk.ACTIVE)
            if not selected:
                messagebox.showwarning("Selection Error", "Please select a note to edit.")
                return

            note_id = selected.split(":")[0]
            new_title = simpledialog.askstring("Edit Title", "Enter new title:", initialvalue=selected.split(":")[1])
            new_content = content_text.get("1.0", tk.END).strip()

            if not new_title or not new_content:
                messagebox.showwarning("Input Error", "Title and content cannot be empty!")
                return

            try:
                query = "UPDATE notes SET title = %s, content = %s WHERE id = %s"
                db_cursor.execute(query, (new_title, new_content, note_id))
                db_connection.commit()
                messagebox.showinfo("Success", "Note updated successfully!")
                view_notes()
                clear_fields()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

        def delete_note():
            selected = notes_list.get(tk.ACTIVE)
            if not selected:
                messagebox.showwarning("Selection Error", "Please select a note to delete.")
                return

            note_id = selected.split(":")[0]
            try:
                query = "DELETE FROM notes WHERE id = %s"
                db_cursor.execute(query, (note_id,))
                db_connection.commit()
                messagebox.showinfo("Success", "Note deleted successfully!")
                view_notes()
                clear_fields()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

        def load_note():
            selected = notes_list.get(tk.ACTIVE)
            if not selected:
                messagebox.showwarning("Selection Error", "Please select a note to load.")
                return

            note_id = selected.split(":")[0]
            try:
                query = "SELECT title, content FROM notes WHERE id = %s"
                db_cursor.execute(query, (note_id,))
                result = db_cursor.fetchone()
                if result:
                    title_entry.delete(0, tk.END)
                    title_entry.insert(tk.END, result[0])
                    content_text.delete("1.0", tk.END)
                    content_text.insert(tk.END, result[1])
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

        def clear_fields():
            title_entry.delete(0, tk.END)
            content_text.delete("1.0", tk.END)

        # Notepad UI
        tk.Label(root, text="Title:").pack(pady=10)
        title_entry = tk.Entry(root, width=50)
        title_entry.pack(pady=5)

        tk.Label(root, text="Content:").pack(pady=10)
        content_text = tk.Text(root, height=10, width=50)
        content_text.pack(pady=5)

        tk.Button(root, text="Add Note", command=add_note).pack(pady=5)
        tk.Button(root, text="View Notes", command=view_notes).pack(pady=5)

        notes_list = tk.Listbox(root, width=50, height=10)
        notes_list.pack(pady=5)
        notes_list.bind("<<ListboxSelect>>", lambda event: load_note())

        tk.Button(root, text="Edit Note", command=edit_note).pack(pady=5)
        tk.Button(root, text="Delete Note", command=delete_note).pack(pady=5)

        # Close database connection when window closes
        root.protocol("WM_DELETE_WINDOW",
                                lambda: [db_cursor.close(), db_connection.close(), root.destroy()])

if __name__ == "__main__":
    root = tk.Tk()
    app = Notes(root)
    root.mainloop()
