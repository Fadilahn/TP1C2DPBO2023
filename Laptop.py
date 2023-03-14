# define class Laptop
class Laptop:
    # deklarasi atribut
    _brand = ""

    # constructor
    def __init__(self, brand):
        self._brand = brand

    # getter
    def getBrand(self):
        return self._brand