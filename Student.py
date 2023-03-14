from Human import Human
from Laptop import Laptop

# define the Student class which inherits from Human
class Student(Human):
    _nim = ""
    _laptop = Laptop("")
    _score = 0

    def __init__(self, name, gender, nim):
        super().__init__(name, gender)
        self._nim = nim
        self._books = []
        self._tasks = []

    def getNim(self):
        return self._nim
    
    def setScore(self, score):
        if self._tasks:
            for i, j in enumerate(self._tasks):
                score -= i+1
                
        self._score = score

    def getScore(self):
        return self._score

    def addBook(self, book):
        if isinstance(book, list):
            self._books.extend(book)
        else:
            self._books.append(book)

    def displayBook(self):
        print("Book list:")
        if self._books:
            for i, book in enumerate(self._books):
                print(f"{i+1}. {book}")

    def addLaptop(self, laptop):
        self._laptop = laptop

    def addTask(self, task):
        self._tasks.append(task)

    def getTask(self, task):
        if isinstance(task, int):
            return self._tasks[task]
        elif isinstance(task, str):
            for i in self._tasks:
                if i == task:
                    return i
        else:
            print("Error")

    def displayTask(self):
        print("Unfinished tasks:")
        if self._tasks:
            for i, task in enumerate(self._tasks):
                print(f"{i+1}. {task}")

    def submitTask(self, task):
        if task == "cheat":
            self._tasks = []
            print(f"{self._name} has submitted all assignment")
        else:
            self._tasks.remove(task)
            print(f"{self._name} has submitted {task}")

    def study(self, subject):
        print(f"{self._name} is studying {subject} using {self._laptop}")

    def displayAll(self):
        print(f"Nama    : {self.getName()}")
        print(f"Gender  : {self.getGender()}")
        print(f"NIM     : {self.getNim()}")
        print(f"Nilai   : {self.getScore()}")
        print(f"Laptop  : {self._laptop.getBrand()}")
        self.displayBook()
        if self._tasks:
            self.displayTask()
            print('=' * 35)

            print("Kamu punya tugas yang belum dikerjakan, kerjakan sekarang? (y/n)")
            choice = input("-> ")
            print('-' * 10)

            if choice.lower() == "y":
                print("Tulis tugas yang belum dikerjakan:")
                while self._tasks:
                    task = input("-> ") 
                    print('-' * 10)
                    if not task:
                        break
                    else:
                        if task in self._tasks:
                            self.submitTask(task)
                            print('=' * 35)


