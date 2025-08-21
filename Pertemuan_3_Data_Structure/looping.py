# for
# digunakan saat kamu tau syarat dan apa yang kamu lakukan tau kapan berhenti
print("=========for===========")
for index in range(2):
    print(f"{index}.Maaf sayang")
# for dengan list
print("=========for+list===========")
angka = ['Satu', 'Dua', 'Tiga', 'Empat', 'Lima']
for value in angka:
    print(f"{value}")

print("======while=======")
# saat kamu tau syarat tapi gak tau kapan berhenti dan syarat akan di check di awal
count = 10
while count <= 10:
    print("error")
    count += 1

count = 1
while count <= 100:
    if(count % 2 ==0):
        count += 1
        continue #skip 1 putaran
    print(count)
    count += 1
    if (count >= 30):
        break #memaksa keluar dari putaran