import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Contoh Layout Pack")
window.geometry("500x600") #besar dari windows yang dimiliki
ttk.Label(window,text="Label Pertama").pack(padx=10,pady=10) #untuk mengatur layout 1 halaman
ttk.Label(window,text="Label Kedua").pack(padx=10,pady=10)
ttk.Label(window,text="Label Ketiga").pack(padx=10,pady=10)
window.mainloop()
