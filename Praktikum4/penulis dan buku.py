class penulis:
    def __init__(self, name):
        self.name = name
        self.judul = judul()

class buku:
    def __init__(self, name):
        self.name = name
        self.judul = judul()
        

class judul:
    def __init__(self):
        self.items = []

    def add_item1(self, item):
        self.items.append(item)
        print("buku1:", item.name)
    def add_item2(self, item):
        self.items.append(item)
        print("buku2:", item.name)
            
    def remove_item(self, item):
        self.items.remove(item)
        

penulis = penulis("  ")
buku1 = buku ("MALAM-TERE LIYE")
buku2 = buku("HARRY POTTER-J.K ROWLING")

print("="*40)
penulis.judul.add_item1(buku1)
penulis.judul.add_item2(buku2)
penulis.judul.items

