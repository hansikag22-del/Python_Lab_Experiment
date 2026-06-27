import tkinter as tk

# Function to handle button click
def click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, text)


# Main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 14", relief=tk.RAISED)
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)

# Run app
root.mainloop()