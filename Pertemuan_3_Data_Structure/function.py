# void function yang tidak memiliki hasil kegiatan
def format_cetak(nama, pekerjaan, gaji):
    print("===================")
    print(f"Nama : {nama}")
    print(f"Pekerjaan : {pekerjaan}")
    print(f"Gaji : {gaji}")
    print("===================")

# non void
# function dimana functionnya menghasilkan nilai tertentu
def check_ganjil(nilai):
    kalkulasi = nilai % 2
    if (kalkulasi == 0):
        return "Genap"
    else:
        return "Ganjil" #ini disebutnya hasil yang ditandai degnan return dan hasil yang dikembalikan

# contoh non void
kalukasi = check_ganjil(99)
print(kalukasi)

profile= [
    {
        "nama" : "Toni",
        "pekerjaan" : "Programming",
        "gaji" : 7000000
    },
    {
        "nama" : "Siska",
        "pekerjaan" : "Programming",
        "gaji" : 7000000
    },
    {
        "nama" : "Albert",
        "pekerjaan" : "Programming",
        "gaji" : 7000000
    },
]

format_cetak(profile[0]['nama'],profile[0]['pekerjaan'],profile[0]['gaji'])
format_cetak(profile[1]['nama'],profile[1]['pekerjaan'],profile[1]['gaji'])
format_cetak(profile[2]['nama'],profile[2]['pekerjaan'],profile[2]['gaji'])

# print("===================")
# print(f"Nama : {profile[0]['nama']}")
# print(f"Pekerjaan : {profile[0]['pekerjaan']}")
# print(f"Gaji : {profile[0]['gaji']}")
# print("===================")
# print(f"Nama : {profile[1]['nama']}")
# print(f"Pekerjaan : {profile[1]['pekerjaan']}")
# print(f"Gaji : {profile[1]['gaji']}")
# print("===================")
# print(f"Nama : {profile[2]['nama']}")
# print(f"Pekerjaan : {profile[2]['pekerjaan']}")
# print(f"Gaji : {profile[2]['gaji']}")