from Human import Human
from Laptop import Laptop
from Assistant import Assistant

# define the Lecturer class which inherits from Human
class Lecturer(Human):
    _nip = ""
    _markers = []
    _laptop = Laptop("")
    _assistants = []
    _taught = False

    def __init__(self, name, gender, nip):
        super().__init__(name, gender)
        self._nip = nip

    def getNip(self):
        return self._nip

    def addMarker(self, marker):
        if isinstance(marker, list):
            self._markers.extend(marker)
        else:
            self._markers.append(marker)

    def displayMarker(self):
        print("Marker list:")
        if self._markers:
            for i, marker in enumerate(self._markers):
                print(f"{i+1}. {marker}")

    def addLaptop(self, laptop):
        self._laptop = laptop

    def addAssistant(self, assistant):
        if isinstance(assistant, Assistant):
            if isinstance(assistant, list):
                self._assistants.extend(assistant)
            else:
                self._assistants.append(assistant)

    def displayAssistant(self):
        print("Assistant:")
        if self._assistants:
            for i, assistant in enumerate(self._assistants):
                print(f"{i+1}. {assistant.getName()}")

    def teach(self, subject):
        print(f"{self._name} is teaching {subject}.")
        self._taught = True
    
    def giveAssignment(self, task, student):
        if self._taught:
            self._taught = False
            if isinstance(student, list):
                for i in student:
                    i.addTask(task)
                print(f"{self._name} is giving {task} to Students.")
            else:
                student.addTask(task)
                print(f"{self._name} is giving {task} to {student.getName()}.")
        else:
            print("You must teach first before giving a assignment!")

    def giveScore(self, score, student):
        student.setScore(score)
        print(f"{self._name} gave {score} to {student._name}.")

    def displayAll(self):
        print(f"Nama    : {self.getName()}")
        print(f"Gender  : {self.getGender()}")
        print(f"NIP     : {self.getNip()}")
        print(f"Laptop  : {self._laptop.getBrand()}")
        self.displayMarker()
        self.displayAssistant()