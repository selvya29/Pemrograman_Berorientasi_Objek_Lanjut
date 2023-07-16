# AssertionError
x = 1
y = 0
assert y != 0, "Invalid Operation"
print(x / y)


# EOFError
try:
    data = input("Masukkan data: ")
except EOFError:
    print("Tidak ada input yang diberikan")
finally:
    print("Program selesai")


# ImportError
try:
    import modul_yang_ada
except ModuleNotFoundError:
    print("Modul tidak ditemukan, pastikan modul_yang_ada sudah diinstal")
else:
    print("Modul berhasil diimpor")


# IndexError
my_list = [1, 2, 3]
try:
    print(my_list[4])
except IndexError:
    print("Index tidak ditemukan di dalam list")


# TypeError
myString = "Hello World"
myNumber = 100
print(myString + myNumber)


