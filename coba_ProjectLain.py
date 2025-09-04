import tkinter as tk
from tkinter import messagebox

FILE_TUGAS = "tugas.txt"

# ======================
# Fungsi Baca & Simpan
# ======================
def baca_tugas():
    tugas = []
    try:
        file = open(FILE_TUGAS, "r")
        for line in file:
            bagian = line.strip().split("|")
            if len(bagian) == 2:
                tugas.append((bagian[0], bagian[1]))
        file.close()
    except FileNotFoundError:
        pass
    return tugas

def simpan_tugas(tugas):
    file = open(FILE_TUGAS, "w")
    for t in tugas:
        file.write(f"{t[0]}|{t[1]}\n")
    file.close()

# ======================
# Fungsi CRUD
# ======================
def muat_tugas():
    listbox.delete(0, tk.END)
    for i, t in enumerate(baca_tugas(), 1):
        listbox.insert(tk.END, f"{i}. {t[0]} - {t[1]}")

def tambah_tugas():
    nama = entry_nama.get()
    deadline = entry_deadline.get()
    if not nama or not deadline:
        messagebox.showwarning("Peringatan", "Nama dan deadline harus diisi!")
        return
    tugas = baca_tugas()
    tugas.append((nama, deadline))
    simpan_tugas(tugas)
    muat_tugas()
    entry_nama.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)

def hapus_tugas():
    try:
        pilihan = listbox.curselection()[0]
        tugas = baca_tugas()
        hapus = tugas.pop(pilihan)
        simpan_tugas(tugas)
        muat_tugas()
        messagebox.showinfo("Info", f"Tugas '{hapus[0]}' dihapus.")
    except:
        messagebox.showwarning("Peringatan", "Pilih tugas dulu!")

def edit_tugas():
    try:
        pilihan = listbox.curselection()[0]
        nama = entry_nama.get()
        deadline = entry_deadline.get()
        if not nama or not deadline:
            messagebox.showwarning("Peringatan", "Nama dan deadline harus diisi!")
            return
        tugas = baca_tugas()
        tugas[pilihan] = (nama, deadline)
        simpan_tugas(tugas)
        muat_tugas()
        messagebox.showinfo("Info", "Tugas berhasil diedit.")
    except:
        messagebox.showwarning("Peringatan", "Pilih tugas dulu!")

# ======================
# GUI Tkinter
# ======================
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Frame input
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama Tugas").grid(row=0, column=0, padx=5)
entry_nama = tk.Entry(frame_input, width=20)
entry_nama.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Deadline").grid(row=1, column=0, padx=5)
entry_deadline = tk.Entry(frame_input, width=20)
entry_deadline.grid(row=1, column=1, padx=5)

# Tombol CRUD
frame_tombol = tk.Frame(root)
frame_tombol.pack(pady=10)

tk.Button(frame_tombol, text="Tambah", command=tambah_tugas).grid(row=0, column=0, padx=5)
tk.Button(frame_tombol, text="Edit", command=edit_tugas).grid(row=0, column=1, padx=5)
tk.Button(frame_tombol, text="Hapus", command=hapus_tugas).grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

muat_tugas()

root.mainloop()
