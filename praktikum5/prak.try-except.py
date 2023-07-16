try:
    a = int(input("Masukkan bilangan pembilang: "))
    b = int(input("Masukkan bilangan penyebut: "))
    c = a / b
    print("Hasil pembagian:", c)
except ZeroDivisionError:
    print("Error: Bilangan penyebut tidak boleh nol")
except ValueError:
    print("Error: Masukkan bilangan bulat")
except:
    print("Error: Terjadi kesalahan")