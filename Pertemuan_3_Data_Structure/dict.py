# data siswa
# inisialisasi
profile = {
    # key : value
    "kelas" : 12,
    "jurusan" : ["IPA", "IPS"],
    "nama_ketua_kelas" : "Tono"
}

# Read
print(f"Seluruh Data : {profile}")
# Read spesifik
print(f"Kelas : {profile['kelas']}")
print(f"Jurusan : {profile['jurusan'][1]}")

# Update
profile["nama_ketua_kelas"] = "Toni"
print(f"Seluruh Data : {profile}")   

del profile["nama_ketua_kelas"]
print(f"Seluruh Data : {profile}")