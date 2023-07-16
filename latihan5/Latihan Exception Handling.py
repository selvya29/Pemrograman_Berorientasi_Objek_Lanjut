#  Mengatasi Type Error
try:
    x = "Hello"
    y = x + 5
except TypeError:
    print("Terjadi kesalahan tipe data, pastikan variabel yang digunakan sudah benar!")

# Mengatasi ZeroDivisionError
# try:
#     x = 10
#     y = x / 0
# except ZeroDivisionError:
#     print("Terjadi kesalahan pembagian dengan nol!")

# Mengatasi FileNotFoundError
# try:
#     with open("file_yang_tidak_ada.txt") as file:
#         data = file.read()
# except FileNotFoundError:
#     print("File yang diminta tidak ditemukan!")

# Mengatasi KeyError
# dictionary = {"satu": 1, "dua": 2, "tiga": 3}
# try:
#     value = dictionary["empat"]
# except KeyError:
#     print("Key yang diminta tidak ditemukan pada dictionary!")

# Mengatasi IndexError
# list_angka = [1, 2, 3]
# try:
#     value = list_angka[4]
# except IndexError:
#     print("Index yang diminta melebihi jumlah elemen dalam list!")

# Mengatasi AttributeError
# class Manusia:
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur
# manusia = Manusia("Andi", 20)
# try:
#     print(manusia.alamat)
# except AttributeError:
#     print("Objek tidak memiliki atribut yang diminta!")

# Mengatasi ValueError
# try:
#     angka = int("bukan_angka")
# except ValueError:
#     print("Terjadi kesalahan konversi nilai ke dalam tipe data yang diinginkan!")

# Mengatasi NameError
# try:
#     print(nama)
# except NameError:
#     print("Variabel yang diminta belum didefinisikan!")

# Mengatasi KeyboardInterrupt
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("Program dihentikan oleh pengguna!")

# Mengatasi MemoryError
# try:
#     data = "                                " * (10**10)
# except MemoryError:
#     print("Memori tidak cukup untuk menampung data yang diminta!")