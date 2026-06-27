import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------

def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row[1])

def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Enter a task!")
        return

    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    entry.delete(0, tk.END)
    load_tasks()

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task_text = listbox.get(selected)

        cursor.execute("DELETE FROM tasks WHERE task=?", (task_text,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task to delete!")

def edit_task():
    try:
        selected = listbox.curselection()[0]
        old_task = listbox.get(selected)
        new_task = entry.get()

        if new_task == "":
            messagebox.showwarning("Warning", "Enter new task!")
            return

        cursor.execute("UPDATE tasks SET task=? WHERE task=?", (new_task, old_task))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task to edit!")

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("Task Manager")
root.geometry("350x400")
root.resizable(False, False)

# Title
tk.Label(root, text="Task Manager", font=("Arial", 16)).pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5, padx=10, fill=tk.X)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Add", width=8, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Edit", width=8, command=edit_task).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Delete", width=8, command=delete_task).grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 12))
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Load existing tasks
load_tasks()

# Run app
root.mainloop()

conn.close()