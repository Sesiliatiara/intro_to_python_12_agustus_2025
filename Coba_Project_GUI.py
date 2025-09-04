import tkinter as tk
from tkinter import messagebox
import os

# Nama file untuk menyimpan tugas
FILE_TUGAS = "tugas.txt"

# List tugas
tugas = []

# Fungsi simpan ke file
def simpan_tugas():
    with open(FILE_TUGAS, "w", encoding="utf-8") as f:
        for t in tugas:
            f.write(t + "\n")

# Fungsi load dari file
def load_tugas():
    if os.path.exists(FILE_TUGAS):
        with open(FILE_TUGAS, "r", encoding="utf-8") as f:
            for line in f:
                nama = line.strip()
                if nama:
                    tugas.append(nama)
                    listbox_tugas.insert(tk.END, nama)

# Fungsi tambah tugas
def tambah_tugas():
    nama_tugas = entry_tugas.get()
    if nama_tugas:
        tugas.append(nama_tugas)
        listbox_tugas.insert(tk.END, nama_tugas)
        entry_tugas.delete(0, tk.END)
        simpan_tugas()
        messagebox.showinfo("Sukses", f"Tugas '{nama_tugas}' berhasil ditambahkan.")
    else:
        messagebox.showwarning("Peringatan", "Nama tugas tidak boleh kosong!")

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
        if nama_baru:
            tugas[indeks] = nama_baru
            listbox_tugas.delete(indeks)
            listbox_tugas.insert(indeks, nama_baru)
            entry_tugas.delete(0, tk.END)
            simpan_tugas()
            messagebox.showinfo("Sukses", f"Tugas berhasil diubah menjadi '{nama_baru}'.")
        else:
            messagebox.showwarning("Peringatan", "Isi tugas baru tidak boleh kosong!")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin diedit!")

# Buat jendela utama
root = tk.Tk()
root.title("Aplikasi Daftar Tugas")
root.geometry("400x450")

# Input tugas
entry_tugas = tk.Entry(root, width=40)
entry_tugas.pack(pady=10)

# Tombol tambah tugas
btn_tambah = tk.Button(root, text="Tambah Tugas", command=tambah_tugas)
btn_tambah.pack(pady=5)

# Tombol edit tugas
btn_edit = tk.Button(root, text="Edit Tugas", command=edit_tugas)
btn_edit.pack(pady=5)

# Listbox untuk menampilkan daftar tugas
listbox_tugas = tk.Listbox(root, width=50, height=15)
listbox_tugas.pack(pady=10)

# Tombol hapus tugas
btn_hapus = tk.Button(root, text="Hapus Tugas", command=hapus_tugas)
btn_hapus.pack(pady=5)

# Load daftar tugas dari file saat aplikasi dijalankan
load_tugas()

# Jalankan aplikasi
root.mainloop()