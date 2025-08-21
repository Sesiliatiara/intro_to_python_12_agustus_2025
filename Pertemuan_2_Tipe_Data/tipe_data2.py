# int
# integer adalah angka bulat
x = 32767
print("ini adalah contoh bilangan integer : {0}".format(x))
# float atau bubble
# bilangan desimal
f = 10.5
print("ini contoh nilai desimal : {0}".format(f))
# kompleks
z = 2 + 3j
print("ini contoh tipe data complex : {0}".format(z))

# sequence type
a = [1, 2, 3, 4]  # list : sifatnya tipe data harus sama semua tidak bisa diubah
print(a)
b = (4,5,6) # truplet : nilainya tidak bisa diubah
print(b)
c = range(0,5) #range : nomer urut
print(c)

# Type Text
# Strings
nama = "Sesilia Tiara Rahayu Ada"

# Mapping type
profile = {"nama" : "Sesilia Tiara Rahayu Ada","age" : 22}
print("Siapakah nama anda : {0}".format(profile["nama"]))

# Set type
f = {1,2,3} #set
print(f)
g = frozenset({4,5,6,7}) #froset
print(g)

# Tipe data konsisi boolean
# Boolean cuman ada 2 nilai True dan False
kondisi_badan = True


# binary type
i = 0b01000001
# desimal = int(i)
# char = chr(desimal)
# print(char)
print(chr(int(i)))  # ubah dari 0b01000001 => 65 ini diubah jadi char A-> print A
j = bytearray(a)    
print(j)
k = memoryview(j)
print(k)