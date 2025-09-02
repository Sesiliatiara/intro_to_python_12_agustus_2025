import tkinter as tk
from tkinter import ttk

# jendela
window = tk.Tk()
window.title("Contoh Penggunaan Label")

label_sapaan = ttk.Label(
    window,
    text = "Selamat datang di GUI baru",
    font = ("Helvetica",10)
)

# tampilkan GUI loop
label_sapaan.pack(padx=20, pady=20 )
window.mainloop()