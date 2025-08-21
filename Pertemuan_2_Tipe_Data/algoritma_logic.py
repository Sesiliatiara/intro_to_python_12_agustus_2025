nilai_raport = 100

# if
# format
# if (kondisi) : 
# apa yang akan kamu lakukan kalau kondisinya terpenuh
print("=============if=============")
if (nilai_raport >= 100): 
    print("Selamat kamu lulus dengan nilai yang sempurna")

nilai_raport = 50
print("============if-else============")
if(nilai_raport >= 60): 
    print("Selamat kamu lulus dalam ujian ini")
else:
    print("Kamu tidak lulus, silahkan lakukan ujian ulang")
# singkatan
# tenery
# kondisinya cuman untuk nilai sesaat atau kondisi yang singkat
print("============tenery if else============")
pesan = "A" if nilai_raport >= 60 else "C"
print ("Nilai kamu : {0}".format(pesan))

print("============if elif else (if else bersarang atau nesterd)============")
nilai_raport = 75
if (nilai_raport >= 90) :
    print("Selamat kamu lulus dengan nilai sempurna")
elif(nilai_raport >= 70 and nilai_raport <= 80):
    if(nilai_raport >= 75):
        print("nilai unik hampir tidak lulus")
    else:
        print("Selamat kamu lulus")
else:
    print("Kamu tidak lulus")

# Switch case
print("============Switch Case============")
print("Selamat datang di menu")
print("1. Start")
print("2. Exit")
select = input("Selection => ")
match select:
    case "1":
        print("Game Start")
    case "2":
        print("Game Over")
    case _:
        print("Input no valid")