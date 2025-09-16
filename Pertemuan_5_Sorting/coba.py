import tkinter as tk
from tkinter import messagebox

# Nama file untuk menyimpan tugas
# FILE_TUGAS = "tugas.txt"

# List tugas (berisi tuple: (nama, deadline))
tugas = []

# Fungsi simpan ke file
def simpan_tugas():
    file = open("./tugas.txt", "w")
    for t in tugas:
        file.write(f"{t[0]}|{t[1]}\n")
    file.close()

# Fungsi load dari file
def load_tugas():
    try:
        file = open("./tugas.txt", "r")
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 2:
                nama, deadline = parts
                tugas.append((nama, deadline))
                listbox_tugas.insert(tk.END, f"{nama} - {deadline}")
        file.close()
    except FileNotFoundError:
        # Kalau file belum ada, biarkan kosong
        pass

# Fungsi tambah tugas
def tambah_tugas():
    nama_tugas = entry_tugas.get()
    deadline = entry_deadline.get()
    if nama_tugas and deadline:
        tugas.append((nama_tugas, deadline))
        listbox_tugas.insert(tk.END, f"{nama_tugas} - {deadline}")
        entry_tugas.delete(0, tk.END)
        entry_deadline.delete(0, tk.END)
        simpan_tugas()
        messagebox.showinfo("Sukses", f"Tugas '{nama_tugas}' berhasil ditambahkan.")
    else:
        messagebox.showwarning("Peringatan", "Nama tugas dan deadline harus diisi!")

# Fungsi hapus tugas
def hapus_tugas():
    try:
        indeks = listbox_tugas.curselection()[0]
        tugas.pop(indeks)
        listbox_tugas.delete(indeks)
        simpan_tugas()
        messagebox.showinfo("Sukses", "Tugas berhasil dihapus.")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

# Fungsi edit tugas
def edit_tugas():
    try:
        indeks = listbox_tugas.curselection()[0]
        nama_baru = entry_tugas.get()
        deadline_baru = entry_deadline.get()
        if nama_baru and deadline_baru:
            tugas[indeks] = (nama_baru, deadline_baru)
            listbox_tugas.delete(indeks)
            listbox_tugas.insert(indeks, f"{nama_baru} - {deadline_baru}")
            entry_tugas.delete(0, tk.END)
            entry_deadline.delete(0, tk.END)
            simpan_tugas()
            messagebox.showinfo("Sukses", f"Tugas berhasil diubah menjadi '{nama_baru} - {deadline_baru}'.")
        else:
            messagebox.showwarning("Peringatan", "Nama tugas dan deadline harus diisi!")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin diedit!")

# Buat jendela utama
window = tk.Tk()
window.title("Aplikasi Daftar Tugas dengan Deadline")
window.geometry("450x500")

# Input tugas
lbl_tugas = tk.Label(window, text="Nama Tugas:")
lbl_tugas.pack()
entry_tugas = tk.Entry(window, width=40)
entry_tugas.pack(pady=5)

lbl_deadline = tk.Label(window, text="Deadline (dd/mm/yyyy):")
lbl_deadline.pack()
entry_deadline = tk.Entry(window, width=40)
entry_deadline.pack(pady=5)

# Tombol tambah tugas
btn_tambah = tk.Button(window, text="Tambah Tugas", command=tambah_tugas)
btn_tambah.pack(pady=5)

# Tombol edit tugas
btn_edit = tk.Button(window, text="Edit Tugas", command=edit_tugas)
btn_edit.pack(pady=5)

# Listbox untuk menampilkan daftar tugas
listbox_tugas = tk.Listbox(window, width=60, height=15)
listbox_tugas.pack(pady=10)

# Tombol hapus tugas
btn_hapus = tk.Button(window, text="Hapus Tugas", command=hapus_tugas)
btn_hapus.pack(pady=5)

# Load daftar tugas dari file saat aplikasi dijalankan
load_tugas()

# Jalankan aplikasi
window.mainloop()
