class Shape:
    def area(self):
        pass

class Beam(Shape):
    def __init__(self, width, height, lengthy):
        self.width = width
        self.height = height
        self.lengthy = lengthy


    def area(self):
        return self.width * self.height * self.lengthy

class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4/3 * 3.14 * self.radius ** 3

beam = Beam(5, 10, 15)
print("Luas Balok:", beam.area())  # Output: Luas Balok: 750

sphere = Sphere(30)
print("Luas Bola:", sphere.area())  # Output: Luas Bola: 113040