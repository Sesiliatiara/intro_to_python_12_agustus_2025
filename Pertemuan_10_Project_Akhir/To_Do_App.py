import os

class ToDoApp:
    def __init__(self, filetugas="tugas.txt"):
        self.file_tugas = filetugas
        self.daftar_tugas = []
        self.read_tugas()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def simpan_tugas(self):
        file = open(self.file_tugas, "w")
        for nama, deadline in self.daftar_tugas:
            file.write(f"{nama}|{deadline}\n")
        file.close()

    def read_tugas(self):
        try:
            file = open(self.file_tugas, "r")   # buka file
            for line in file:                 # baca tiap baris
                parts = line.strip().split("|")
                if len(parts) == 2: 
                    nama, deadline = parts
                    self.daftar_tugas.append((nama, deadline))
            file.close()
        except FileNotFoundError:
            # kalau file belum ada, biarkan kosong
            pass

    def tambah_tugas(self, tugas_baru, deadline):
        self.daftar_tugas.append((tugas_baru, deadline))
        self.simpan_tugas()
        print(f"Tugas {tugas_baru} dengan (Deadline: {deadline}) berhasil ditambahkan")
        input("Tekan Enter untuk melanjutkan...")
        self.clear_screen()

    def lihat_tugas(self):
        if not self.daftar_tugas:
            print("Tidak ada tugas saat ini")
        else:
            print("\nDaftar Tugas:")
            for i in range(len(self.daftar_tugas)):
                nama, deadline = self.daftar_tugas[i]
                print(f"{i+1}. {nama} (Deadline: {deadline})")
        input("Tekan Enter untuk melanjutkan...")
        self.clear_screen()

    def hapus_tugas(self, nomor_tugas):
        try:
            indeks_tugas = int(nomor_tugas) - 1
            if 0 <= indeks_tugas < len(self.daftar_tugas):
                tugas_dihapus = self.daftar_tugas.pop(indeks_tugas)
                self.simpan_tugas()
                print(f"Tugas {tugas_dihapus} berhasil dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Masukkan harus berupa angka.")
        input("Tekan Enter untuk melanjutkan...")
        self.clear_screen()

    def edit_tugas(self, nomor_tugas, tugas_baru, deadline_baru):
        try:
            indeks_tugas = int(nomor_tugas) - 1
            if 0 <= indeks_tugas < len(self.daftar_tugas):
                tugas_lama = self.daftar_tugas[indeks_tugas]
                self.daftar_tugas[indeks_tugas] = (tugas_baru, deadline_baru)
                self.simpan_tugas()
                print(f"Tugas {tugas_lama} berhasil diubah menjadi {tugas_baru} (Deadline: {deadline_baru}).")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Masukkan harus berupa angka.")
        input("Tekan Enter untuk melanjutkan...")
        self.clear_screen()

    def main(self):
        while True:
            self.clear_screen()
            print("\n===== Menu Aplikasi To Do List ======")
            print("1. Tambah Tugas")
            print("2. Lihat Tugas")
            print("3. Edit Tugas")
            print("4. Hapus Tugas")
            print("5. Exit")
            selection = input("Pilih menu (1/2/3/4/5): ")
            try:
                selection = int(selection)
                match selection:
                    case 1:
                        tugas_baru = input("Masukkan nama tugas: ")
                        deadline_baru = input("Masukkan deadline (YYYY-MM-DD): ")
                        self.tambah_tugas(tugas_baru, deadline_baru)
                    case 2:
                        self.lihat_tugas()
                    case 3:
                        self.lihat_tugas()
                        nomor_tugas = input("Masukkan nomor tugas yang ingin diubah: ")
                        tugas_baru = input("Masukkan nama tugas baru: ")
                        deadline_baru = input("Masukkan deadline baru (YYYY-MM-DD): ")
                        self.edit_tugas(nomor_tugas, tugas_baru, deadline_baru)
                    case 4:
                        nomor_tugas = input("Masukkan nomor tugas yang ingin dihapus: ")
                        self.hapus_tugas(nomor_tugas)
                    case 5:
                        print("Terima kasih! Aplikasi To Do List ditutup.")
                        break
                    case _:
                        print("Invalid Input")
            except ValueError:
                print("Mohon masukkan angka, bukan huruf!!")