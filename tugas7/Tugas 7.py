class BMI:
    def __init__(self, berat, tinggi):
        self.berat = berat
        self.tinggi = tinggi
        
    def hitung_bmi(self):
        return self.berat / (self.tinggi ** 2)
        
    def bmi_status(self, bmi):
        if bmi < 18.5:
            return "Kekurangan Berat Badan"
        elif bmi < 25:
            return "Normal (Ideal)"
        elif bmi < 30:
            return "Kelebihan Berat Badan"
        else:
            return "Obesitas"
        
class BMIMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        
    def tinggi_berat(cls, tinggi, berat):
        return cls(berat, tinggi)
        
    def tinggi_bmi_status(cls, tinggi, bmi_status):
        if bmi_status == "Kekurangan Berat Badan":
            bmi = 18.4
        elif bmi_status == "Normal (Ideal)":
            bmi = 24.9
        elif bmi_status == "Kelebihan Berat Badan":
            bmi = 29.9
        else:
            bmi_status == "Obesitas"
            bmi = 35.0
        berat = bmi * (tinggi ** 2)
        return cls(berat, tinggi)

class BMI(BMI, metaclass=BMIMeta):
    pass

# Menghitung BMI dan menentukan status BMI berdasarkan tinggi badan dan berat badan
bmi = BMI.tinggi_berat(1.60, 55)
print("BMI:", bmi.hitung_bmi())
print("Status BMI:", bmi.bmi_status(bmi.hitung_bmi()))
