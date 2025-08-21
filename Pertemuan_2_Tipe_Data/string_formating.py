nama = "Tiara"
nik = 2142003
kota = "Bekasi"
tanggal = "24 November 2024"
tanggal_start = "25 November 2024"
tanggal_end = "27 November 2024"
hari = "2 hari"

hal = "Permohonan cuti sakit"


# posisonal argument
print("Hello {0}\nBerapakah usia anda : {1}\nAlamat anda di mana? {2}".format(nama, kota, nik))
print()
# keyword argumen
# \n = new line atau enter
# \t = untuk tab standar (4 spasi)
print("{lokasi}, {tanggal}\nPerihal:{perihal}\n\nYth, \nKepala HRD PT Visi Maju\nDi tempat\n\nDengan hormat, \nYang bertanda tangan di bawah ini :\nNama: {nama}\nNIK: {nik}\n\nBermaksud mengajukan cuti tahunan selama {hari},\nterhitung mulai tanggal {tanggal_start} sampai {tanggal_end}\nDemikian surat permohonan cuti ini saya ajukan.\nAtas perhatian Bapak/Ibu, saya ucapkan terimakasih.".format(tanggal=tanggal, lokasi=kota, perihal=hal, hari=hari, nama=nama, nik=nik, tanggal_start=tanggal_start, tanggal_end=tanggal_end))
print("\n\n Hormat Saya.\n{nama}".format(nama = nama))