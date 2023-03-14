class CRUD:
    def __init__(self):
        self.data = []
    
    def add(self, obj):
        self.data.append(obj)
    
    def get_all(self):
        return self.data

class Table:
    def __init__(self, data):
        self.data = data
    
    def display(self):
        if not self.data:
            print("No data to display.")
            return

        # determine the maximum width of each column
        num_columns = len(self.data[0])
        column_widths = [max(len(str(row[i])) for row in self.data) for i in range(num_columns)]
        column_widths.insert(0, len(str(len(self.data) - 1)))  # add width for "NO" column
        
        # create the header row
        header_row = '+'.join(['-' * (width + 2) for width in column_widths])
        print(header_row)
        header = '| ' + ' | '.join(str(i).ljust(column_widths[n]) for n, i in enumerate(["NO"] + list(self.data[0].keys()))) + ' |'
        print(header)
        print(header_row)

        # create the data rows
        for index, row in enumerate(self.data, start=1):
            data = '| ' + ' | '.join(str(i).ljust(column_widths[n]) for n, i in enumerate([index] + list(row.values()))) + ' |'
            print(data)
        
        print(header_row)

# define a Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# create a CRUD object for Student data
student_crud = CRUD()

# add some sample data
student_crud.add(Student("Alice", 18, "A"))
student_crud.add(Student("Bob", 17, "B"))
student_crud.add(Student("Charlie", 16, "C"))

# retrieve all student data from the CRUD object
students = student_crud.get_all()

# create a Table object and display the data
table = Table([vars(student) for student in students])
table.display()
