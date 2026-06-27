import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------

def signup():
    username = signup_user.get()
    password = signup_pass.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Account Created!")
    except:
        messagebox.showerror("Error", "Username already exists!")

def login():
    username = login_user.get()
    password = login_pass.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Credentials!")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Login & Signup System")
root.geometry("350x400")
root.resizable(False, False)

# Title
tk.Label(root, text="Authentication System", font=("Arial", 16)).pack(pady=10)

# ---------------- LOGIN SECTION ----------------
tk.Label(root, text="Login", font=("Arial", 14)).pack(pady=5)

login_user = tk.Entry(root)
login_user.pack(pady=2)
login_user.insert(0, "Username")

login_pass = tk.Entry(root, show="*")
login_pass.pack(pady=2)
login_pass.insert(0, "Password")

tk.Button(root, text="Login", command=login, bg="blue", fg="white").pack(pady=5)

# ---------------- SIGNUP SECTION ----------------
tk.Label(root, text="Signup", font=("Arial", 14)).pack(pady=10)

signup_user = tk.Entry(root)
signup_user.pack(pady=2)
signup_user.insert(0, "Username")

signup_pass = tk.Entry(root, show="*")
signup_pass.pack(pady=2)
signup_pass.insert(0, "Password")

tk.Button(root, text="Signup", command=signup, bg="green", fg="white").pack(pady=5)

# Run app
root.mainloop()

conn.close()