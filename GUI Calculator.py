import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Set the dimensions of the window
root.geometry("300x500")

# Entry widget to display the input and output
display = tk.Entry(root, font=("Arial", 15), borderwidth=5, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Global variable to store the current input and result
current_input = ""


# Function to update the display when a button is clicked
def button_click(item):
    global current_input
    current_input += str(item)
    display.delete(0, tk.END)
    display.insert(tk.END, current_input)


# Function to clear the display
def clear_display():
    global current_input
    current_input = ""
    display.delete(0, tk.END)


# Function to evaluate the expression
def evaluate_expression():
    global current_input
    try:
        result = str(eval(current_input))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        current_input = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        current_input = ""


# Defining button texts in window
buttons = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', '.', '=', '+',
]

# Creating buttons in window to display options
row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, font=("Arial", 10), command=evaluate_expression)
    elif button == "C":
        btn = tk.Button(root, text=button, font=("Arial", 10), command=clear_display)
    else:
        btn = tk.Button(root, text=button, font=("Arial", 10), command=lambda b=button: button_click(b))

    btn.grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=20, ipady=20)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Creating a Clear Button in display
clear_btn = tk.Button(root, text='C', font=("Arial", 10), command=clear_display)
clear_btn.grid(row=row_val, column=0, columnspan=4, padx=5, pady=5, ipadx=20, ipady=20)

# Running the application
root.mainloop()
