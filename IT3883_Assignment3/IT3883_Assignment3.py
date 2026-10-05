# IT3883_Assignment3.py
# IT3883/Section W01
# Austin Gurley
# Assignment 3
# Due Date: 10/10/2026
# A GUI application that converts Miles per Gallon (mpg) into
# Kilometers per Liter (km/l). The result updates automatically
# with every keystroke, so no button is needed. Blank or
# non-numeric input is handled without crashing.
# 
# Python tkinter documentation (https://docs.python.org/3/library/tkinter.html)

import tkinter as tk

# Conversion factor given in the assignment: 1 mpg = 0.425143707 km/l
MPG_TO_KML = 0.425143707

def convert(*args):
    """
    Read the mpg entry box, convert it, and update the result label.
    Called automatically every time the text in the entry box changes.
    *args absorbs the three arguments tkinter passes to trace callbacks.
    """
    text = mpg_var.get().strip()

    # Blank box: clear the result instead of showing an error
    if text == "":
        result_var.set("")
        return

    # float() raises ValueError on letters/symbols, so catch it here. rather than letting the program crash
    try:
        mpg = float(text)
    except ValueError:
        result_var.set("Please enter a number")
        return

    # Valid number: do the conversion and show it to 4 decimal places
    kml = mpg * MPG_TO_KML
    result_var.set(f"{kml:.4f} km/l")


# Main window setup
root = tk.Tk()
root.title("MPG to KM/L Converter")
root.resizable(False, False)

# StringVars link the widgets to values we can read and update in code
mpg_var = tk.StringVar()
result_var = tk.StringVar()

# Run convert() whenever mpg_var is written to
# This is what makes the result update live without a button.
mpg_var.trace_add("write", convert)

# Widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Input row: label + entry box for miles per gallon
tk.Label(frame, text="Miles per Gallon:").grid(row=0, column=0, sticky="e", pady=5)
mpg_entry = tk.Entry(frame, textvariable=mpg_var, width=20)
mpg_entry.grid(row=0, column=1, padx=10, pady=5)

# Output row: label + read-only result that tracks result_var
tk.Label(frame, text="Kilometers per Liter:").grid(row=1, column=0, sticky="e", pady=5)
tk.Label(frame, textvariable=result_var, width=20, anchor="w").grid(
    row=1, column=1, padx=10, pady=5
)

# Put the cursor in the entry box so the user can start typing right away
mpg_entry.focus()

# Start the event loop (keeps the window open and responsive)
root.mainloop()