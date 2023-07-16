class BolaMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        
        def volume(cls, jari_jari):
            return 4/3 * 3.14 * jari_jari ** 3
        cls.volume = classmethod(volume)
        
        def luas_permukaan(cls, jari_jari):
            return 4 * 3.14 * jari_jari ** 2
        cls.luas_permukaan = classmethod(luas_permukaan)

class Bola(metaclass=BolaMeta):
    pass

b = Bola()
jari_jari = 8

volume = b.volume(jari_jari)
print(f"Volume bola: {volume:.2f} cm^3")

luas_permukaan = b.luas_permukaan(jari_jari)
print(f"Luas permukaan bola : {luas_permukaan:.2f} cm^2")
