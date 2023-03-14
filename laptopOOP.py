class Laptop:
def __init__(self, brand, type):
self.brand = brand
self.type = type
def info(self):
print(f"Brand: {self.brand}\nType: {self.type}")
laptopA = Laptop("Asus", "K331S")
laptopA.info()