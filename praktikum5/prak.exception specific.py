try:
    num_list = [1, 2, 3, 4, 5]
    index = int(input("Masukkan indeks: "))
    num = num_list[index]
    print("Angka pada indeks tersebut adalah:", num)
except IndexError:
    print("Error: Indeks yang dimasukkan tidak valid")
except ValueError:
    print("Error: Masukkan angka")
except:
    print("Error: Terjadi kesalahan saat memproses input")
