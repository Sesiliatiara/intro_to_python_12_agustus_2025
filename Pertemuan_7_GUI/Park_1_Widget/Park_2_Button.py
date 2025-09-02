import tkinter as tk
from tkinter import ttk

# function
def sapaan():
    print("Button berhasil di click!")

# jendela
window = tk.Tk()
window.title("Contoh Penggunaan Button")

# isi content
button_sapaan = tk.Label(
    window,
    text="Click Here!!!",
    font=("Helvetica", 10)
)
button_click = ttk.Button(
    window,
    text="Click ",
    command=sapaan
)

label_sapaan = ttk.Label(
    window,
    text = "Selamat datang di GUI baru",
    font = ("Helvetica",10)
)

# tampilkan GUI loop
label_sapaan.pack(padx=20, pady=20 )
button_click.pack(padx=20, pady=20)
window.mainloop()