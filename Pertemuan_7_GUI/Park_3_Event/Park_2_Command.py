import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("contoh bind command")

def panggilan():
    print("Hello World!!")

tombol = ttk.Button(window, text="Click Here!!", command=panggilan)
tombol.pack(padx=100, pady=100)

window.mainloop()