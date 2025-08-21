# example buah
# dalam programming konsep dasarnya disebut CRUD
#  C = Create (Membuat)
#  R = Read (Membaca)
#  U = Update (Memperbarui)
#  D = Delete (Menghapus)

buah = ["Salah pondo"] # ini sebutannya instansiasi (mempersiapkan benda apa yang disimpan)

# Add (Create)
buah.append("Satu")
buah.append("Dua")
buah.append("Tiga")
buah.append("Empat")

# Read
print(f"Memanggil Semua List : {buah}")
# Read Spesifik nilai
print(f"Index ke 3 : {buah[-1]}")

# Update
buah[0] = "Nol"
print(f"Memanggil Semua List : {buah}")

# Delete
del buah[0]
print(f"Memanggil Semua List : {buah}")