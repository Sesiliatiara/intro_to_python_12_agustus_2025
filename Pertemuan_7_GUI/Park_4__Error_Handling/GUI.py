import tkinter as tk
from tkinter import ttk,messagebox

window = tk.Tk()
window.title("Contoh bind command")

def penjumlahan():
    try:
        x = float(value1.get())
        y = float(value2.get())
        hasil = x / y 
        hasil_lebel.grid(row=3,column=0,columnspan=2,padx=5 ,pady=5)
        hasil_lebel.config(text=f"Hasil: {hasil}")  
    except ValueError:
        messagebox.showerror("Input Salah", "Harap Masukan Angka Yang valid")
    except ZeroDivisionError:
        messagebox.showerror("Kesalahan matematika","Tidak bisa membagi dengan nol")

ttk.Label(window,text="Masukan nilai : ").grid(row=0,column=0,sticky="w",padx=5,pady=5)
value1 = ttk.Entry(window,)
value1.grid(row=0,column=1,padx=5,pady=5)
ttk.Label(window,text="Masukan pembagi : ").grid(row=1,column=0,sticky="w",padx=5,pady=5)
value2 = ttk.Entry(window,)
value2.grid(row=1,column=1,padx=5,pady=5)
hasil_lebel = ttk.Label(window,text="")
ttk.Button(window,text="Hasil",command=penjumlahan).grid(row=2,column=0,columnspan=2,padx=5,pady=5)
window.mainloop()