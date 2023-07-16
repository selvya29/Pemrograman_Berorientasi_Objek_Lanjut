try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Error: File tidak ditemukan")
except:
    print("Error: Terjadi kesalahan saat membaca file")
finally:
    file.close()
    print("File ditutup")
