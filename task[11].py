import tkinter as tk

# Function to update the expression
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display expressions
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                        command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                        command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', width=5, height=2, font=("Arial", 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)

# Run the application
root.mainloop()
