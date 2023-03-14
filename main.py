# import class from file
from Student import Student
from Lecturer import Lecturer
from Assistant import Assistant
from BEM import BEM, BEMMember
from EnglishClub import EnglishClub, EnglishClubMember
from Simulation import Simulation
from Laptop import Laptop

# add data laptop
lenovo = Laptop("Lenovo")
asus = Laptop("Asus")
mac = Laptop("Mac")
hp = Laptop("HP")
acer = Laptop("Acer")
laptop = [lenovo, asus, mac, hp, acer]

# create some objects based on the classes
resyad = Student("Resyad", "L", "21001")
pahri = BEMMember("Pahri", "L", "21002")
angga = EnglishClubMember("Angga", "L", "21003")
getsbi = EnglishClubMember("Getsbi", "L", "21004")
mila = Assistant("Mila", "P", "5")
rose = Lecturer("Mrs. Rose", "p", "1")
rose.addLaptop(mac)
rose.addMarker(["Black", "Red", "Blue"])
rose.addAssistant(mila)

# create a list of students and lecturer
students = [resyad, pahri, angga, getsbi, mila]
lecturers = [rose]

# add laptop to students
for i, student in enumerate(students):
    student.addLaptop(laptop[i])

# add data book
books = ["Math", "English", "History", "Biology", "Chemistry", "Physics", 
         "Geography", "Economics", "Computer Science", "Statistics"]

# add book to student
i = 0
for student in students:
    student.addBook([books[i], books[i+1]])
    i += 2

# add BEM
kemakom = BEM("Kemakom")
kemakom.add_member(pahri)

# add English Club
ec = EnglishClub()
ec.add_member(angga)
ec.add_member(getsbi)

# add proker for organization
prokerBEM = ["Seminar Nasional Informatika",
             "Pelatihan Desain Grafis",
             "Pengabdian Masyarakat",
             "Sosialisasi Beasiswa",
             "Lomba Gemastik"]

prokerEC = ["English Conversation Practice",
            "English Reading Club",
            "English Writing Workshop",
            "English Movie Night",
            "English Public Speaking Seminar"]

kemakom.add_proker(prokerBEM)
ec.add_proker(prokerEC)

# Run Simulation of this system
simulation = Simulation(lecturers, students, kemakom, ec)
simulation.choiceStart()






