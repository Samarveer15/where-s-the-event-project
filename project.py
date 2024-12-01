import tkinter as tk
from tkinter import ttk

def convert_length():
    try:
        length_in_meters = float(entry.get())
        length_in_feet = length_in_meters * 3.28084
        result_label.config(text=f"{length_in_meters} meters is {length_in_feet:.2f} feet")
    except ValueError:
        result_label.config(text="Please enter a valid number")

root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

ttk.Label(root, text="Enter length in meters:").pack(pady=10)
entry = ttk.Entry(root)
entry.pack(pady=10)

convert_button = ttk.Button(root, text="Convert", command=convert_length)
convert_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
