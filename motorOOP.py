class Motor:
def __init__(self, brand, warna):
self.brand = brand
self.warna = warna
def info(self):
print(f"Motor {self.brand} berwarna {self.warna}")
motorA = Motor("Honda", "Putih")
motorA.info() 
# Output: Mo=tor Honda berwarna Putih