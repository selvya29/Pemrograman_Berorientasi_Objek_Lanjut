class KerucutMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def volume(cls, jari_jari, tinggi):
            return (3.14 * jari_jari ** 2 * tinggi) / 3
        cls.volume = classmethod(volume)

        def luas_permukaan(cls, jari_jari, sisi_miring):
            return 3.14 * jari_jari * (jari_jari + sisi_miring)
        cls.luas_permukaan = classmethod(luas_permukaan)

class Kerucut(metaclass=KerucutMeta):
    pass

k = Kerucut()

volume_kerucut = k.volume(4, 12)
print("Volume kerucut:", volume_kerucut)

luas_permukaan_kerucut = k.luas_permukaan(2, 10)
print("Luas permukaan kerucut:", luas_permukaan_kerucut)
