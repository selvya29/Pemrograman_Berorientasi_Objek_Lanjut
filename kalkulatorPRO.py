class Kalkulator:
@staticmethod
def add(x, y):
return x + y
@staticmethod
def subtract(x, y):
return x - y
@staticmethod
def multiply(x, y):
return x * y
@staticmethod
def divide(x, y):
if y == 0:
raise ValueError('Tidak dapat membagi dengan nol.')
return x / y
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(5, 10)) # Output: 15
print(Kalkulator.subtract(9, 5)) # Output: 4
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(5, 5)) # Output: 25
print(Kalkulator.divide(15, 3)) # Output: 5.0