import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create database and table
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT,
    phone TEXT
)
""")
conn.commit()


# Function to insert data
def register():
    name = name_entry.get()
    email = email_entry.get()
    course = course_entry.get()
    phone = phone_entry.get()

    if name == "" or email == "" or course == "" or phone == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    cursor.execute("INSERT INTO students (name, email, course, phone) VALUES (?, ?, ?, ?)",
                   (name, email, course, phone))
    conn.commit()

    messagebox.showinfo("Success", "Student Registered Successfully!")

    # Clear fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


# GUI Window
root = tk.Tk()
root.title("Student Registration System")
root.geometry("400x400")
root.resizable(False, False)

# Labels & Entries
tk.Label(root, text="Student Registration Form", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Register Button
tk.Button(root, text="Register", command=register, bg="green", fg="white").pack(pady=20)

# Run App
root.mainloop()

# Close DB when app closes
conn.close()
