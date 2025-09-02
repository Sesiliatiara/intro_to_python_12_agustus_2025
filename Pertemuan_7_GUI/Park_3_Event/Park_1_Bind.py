import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("contoh bind command")

def panggilan(event):
    print("Hello World!!")

label = ttk.Label(window, text="Arahkan kursor ke sini ada pesan yang akan muncul")
label.bind("<Enter>", panggilan)
label.pack(padx=20, pady=20)

window.mainloop()