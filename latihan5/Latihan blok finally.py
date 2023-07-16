try:
    file = open('file.txt', 'r')
    num = int(file.readline())
    print('Number:', num)
except ValueError:
    print('Error: Invalid input!')
finally:
    file.close()
    print('File closed.')
