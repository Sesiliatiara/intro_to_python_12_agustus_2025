x = 3
y = 2
# Penjumlahan
hasil = x + y
print("Hasil penjumalhan dari {x} + {y} = {hasil}".format(x = x, y = y, hasil = hasil))
# Pengurangan
hasil = x - y
print("Hasil pengurangan dari {x} - {y} = {hasil}".format(x = x, y = y, hasil = hasil))
# Perkalian
hasil = x * y
print("Hasil perkalian dari {x} x {y} = {hasil}".format(x = x, y = y, hasil = hasil))
# Pembagian
hasil = x / y
hasil_conversi_ke_integer = int(x/y)
print("hasil pembagian dari {x} / {y} = {hasil}".format(x=x, y=y, hasil=hasil))
# Modulus
hasil = x % y
print("Hasil modulus dari {x} % {y} = {hasil}".format(x=x, y=y, hasil=hasil))
# Perpangkatan
hasil = x ** y
print("Hasil pangkat dari {x}^{y} = {hasil}".format(x=x, y=y, hasil=hasil)) 

# Cara menyingkat penjumlahan atau pengurangan
# Increment
z = 0
print("Hasil sebelum ditambahkan : {0}".format(z))
# z = z + 3 (old version)
# z ++
z+=3 # z = z + 3 => z = 0 + 3
print("Hasil z setelah ditambahkan : {0}".format(z))
z-=1 # z = z - 1 => z = 3 - 1
print("Hasil z setelah di kurangkan : {0}".format(z))