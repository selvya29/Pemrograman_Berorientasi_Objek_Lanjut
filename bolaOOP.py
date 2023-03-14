class Bola:
def __init__(self, jari_jari):
self.jari_jari = jari_jari
def volume(self):
return 4/3 * 3.14 * (self.jari_jari ** 3)
bolaA = Bola(14)
print(f"volume bola: {bolaA.volume()}")