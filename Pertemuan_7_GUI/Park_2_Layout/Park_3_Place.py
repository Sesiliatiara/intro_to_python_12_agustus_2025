import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Contoh Layout Place")
window.geometry("400x500") #besar dari windows yang dimiliki
tombol_satu = ttk.Button(window, text="Tombol di posisi koordinat (x = 30, y = 50)")
tombol_satu.place(x=30, y=50)
tombol_dua = ttk.Button(window, text="Tombol di posisi koordinat (x = 100, y = 100)")
tombol_dua.place(x=100, y=100)
window.mainloop()
