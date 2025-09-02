import tkinter as tk
from tkinter import ttk

# function
def sapaan():
    data_input = input_username.get()
    print(f"Username: {data_input}")

# jendela
window = tk.Tk()
window.title("Contoh Penggunaan Button")

# isi content
label_sapaan = ttk.Label(
    window,
    text="Username",
    font=("Helvetica", 10)
)
button_click = ttk.Button(
    window,
    text="Click ",
    command=sapaan
)

input_username = ttk.Entry(
    window,
    width=30
)

# tampilkan GUI loop
label_sapaan.pack(padx=20, pady=20)
input_username.pack(padx=20, pady=20)
button_click.pack(padx=20, pady=20)
window.mainloop()