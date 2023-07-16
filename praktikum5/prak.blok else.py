try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("Error: File tidak ditemukan")
else:
    data = file.read()
    file.close()
    print("Isi file:")
    print(data)
