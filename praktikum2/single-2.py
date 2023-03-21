class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bermain(self):
        print(self.nama, "sedang bermain bola")
class Anjing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def berjenis(self):
       print(self.nama, "merupakan anjing berjenis", self.jenis_bulu, "berumur", self.umur, "tahun")
anjingA = Anjing("Bubu", 3, "Bernese")
anjingA.bermain()
anjingA.berjenis() 