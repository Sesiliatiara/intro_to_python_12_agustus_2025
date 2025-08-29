import random

def generate_random_number(max_value): 
    random_value = []

    for i in range(max_value):
        tmp_value = random.randint(1, 100)
        random_value.append(tmp_value)
    return random_value

def bubble_sort(data):
    length = len(data)
    for index in range(length):
        for value in range(0, length-index-1):
            if data[value] > data[value + 1]:
                tmp = data[value]
                data[value] = data[value + 1]
                data[value + 1] = tmp

def selection_sort(data):
    length = len(data)
    for index in range(length):
        max_index = index
        for value in range(index + 1, length):
            if data[value] < data[max_index]:
                max_index = value
        data[index], data[max_index] = data[max_index], data[index]

def insert_sort(data):
    for index in range(1, len(data)):
        kunci = data[index]
        value= index-1
        # and (&&)
        # or (||)
        while value >=0 and kunci < data[value]:
            data[value+1] = data[value]
            value -= 1
        data[value + 1] = kunci

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        kiri = data[:mid]
        kanan = data[mid:]

        # rekursif
        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i+=1
            else:
                data[k] = kanan[j]
                j+=1
            k +=1

        while i < len(kiri):
            data[k] = kiri[i]
            i+=1
            k+=1

        while j < len(kanan):
            data[k] = kanan[j]
            j+=1
            k+=1


def main():
    # bikin random nilai
    # inisialisasi
    max_input = int(input("Masukkan jumlah angka : "))
    random_value = generate_random_number(max_input)
    print(f"List saat ini : {random_value}")
    input("please enter to next step.........")
    merge_sort(random_value)
    # insert_sort(random_value)
    # selection_sort(random_value)
    # bubble_sort(random_value)
    print(f"Setelah di shorting : {random_value}")

    
if __name__ == "__main__":
    main()