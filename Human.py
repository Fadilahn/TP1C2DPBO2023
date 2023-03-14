# define the base class Human
class Human:
    # deklarasi atribut
    _name = ""
    _gender = ""

    # construktor langsung
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

    # getter
    def getName(self):
        return self._name
    
    def getGender(self):
        return self._gender

    # method makan
    def eat(self):
        print(f"{self._name} is eating.")

    # method minum
    def drink(self):
        print(f"{self._name} is drinking.")

    # method tidur
    def sleep(self):
        print(f"{self._name} is sleeping.")