import tkinter as tk

def button_click(number):
    current = entry_var.get()
    entry_var.set(current + str(number))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main Tkinter window
root = tk.Tk()
root.title("Numpad in Box")

# Create a LabelFrame to hold the numpad with a border
numpad_frame = tk.LabelFrame(root, text="Numpad", padx=10, pady=10)
numpad_frame.pack(padx=10, pady=10)

# Create a Frame to hold the buttons
buttons_frame = tk.Frame(numpad_frame)
buttons_frame.pack()

# Entry widget for displaying the numbers
entry_var = tk.StringVar()
entry = tk.Entry(numpad_frame, textvariable=entry_var, font=('Arial', 14), justify='right')
entry.pack(pady=10)

# Buttons for the numpad
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

for row_buttons in buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack(side=tk.TOP)
    
    for text in row_buttons:
        btn = tk.Button(row_frame, text=text, font=('Arial', 12), padx=20, pady=20, command=lambda t=text: button_click(t))
        btn.pack(side=tk.LEFT, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
