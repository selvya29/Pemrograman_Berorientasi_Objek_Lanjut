class KeretaApi:
def __init__(self, stasiun, tujuan):
self.stasiun = stasiun
self.tujuan = tujuan
def info(self):
print(f"Stasiun: {self.stasiun}\nTujuan: {self.tujuan}")
keretaA = KeretaApi("Express123", "Jakarta - Semarang")
keretaA.info()