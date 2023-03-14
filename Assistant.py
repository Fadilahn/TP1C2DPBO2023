# Import the Student class from Student module
from Student import Student

# Define the Assistant class which inherits from Student
class Assistant(Student):
    _taught = False

    def __init__(self, name, gender, nim):
        super().__init__(name, gender, nim)

    def teach(self, subject):
        # Teach a subject
        print(f"{self._name} is teaching {subject}.")
        self._taught = True

    def giveAssignment(self, task, student):
        # Check if the assistant has taught before giving an assignment
        if self._taught:
            self._taught = False
            # Check if the student parameter is a list of Student objects
            if isinstance(student, list):
                for i in student:
                    i.addTask(task)
                print(f"{self._name} is giving {task} to Students.")
            else:
                student.addTask(task)
                print(f"{self._name} is giving {task} to {student.getName()}.")
        else:
            print("You must teach first before giving an assignment!")