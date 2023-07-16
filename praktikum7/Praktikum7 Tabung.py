class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        def volume(cls, jari_jari, tinggi):
            return 3.14 * jari_jari ** 2 * tinggi

        def luas_permukaan(cls, jari_jari, tinggi):
            return 2 * 3.14 * jari_jari * (jari_jari + tinggi)

        cls.volume = classmethod(volume)
        cls.luas_permukaan = classmethod(luas_permukaan)

class Tabung(metaclass=TabungMeta):
    pass

t = Tabung()

volume_tabung = t.volume(4, 8)
print("Volume tabung:", volume_tabung)

luas_permukaan_tabung = t.luas_permukaan(6, 8)
print("Luas permukaan tabung:", luas_permukaan_tabung)
