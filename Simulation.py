from BEM import BEM, BEMMember
from EnglishClub import EnglishClub, EnglishClubMember
from Assistant import Assistant

class Simulation:
    _lecturer = None
    _lecturers = []
    _student = None
    _students = []
    _bem = BEM("")
    _englishClub = EnglishClub()
    
    def __init__(self, lecturers, students, bem, englishClub):
        self._lecturers = lecturers
        self._students = students
        self._bem = bem
        self._englishClub = englishClub

    def BEMSimulation(self):

        while True:
            # Menampilkan pilihan untuk memilih aksi untuk member yang dipilih
            print(f"Hallo {self._student.getName()}, selamat datang di BEM {self._bem.getName()}")
            print('-' * 35)
            print("Apa yang ingin kamu lakukan hari ini?")
            print("1. Menampilkan Proker")
            print("2. Merancang Proker")
            print("3. Melaksanakan Proker")
            print("4. Mengikuti Evaluasi")
            print("0. Exit")
            print('=' * 35)

            # Meminta input dari user untuk memilih aksi
            choice = int(input("-> "))
            print('-' * 10)

            # Jika user memilih kembali ke pemilihan member, keluar dari loop while
            if choice == 0:
                break

            # Jika user memilih menampilkan tugas saat ini, tampilkan proker yang sedang berjalan
            elif choice == 1:
                self._bem.displayProkers()
                print('=' * 35)

            # Jika user memilih desain tugas, meminta input dari user untuk nama proker dan mendesain proker tersebut
            elif choice == 2:
                print("Masukan nama Proker:")
                proker = input("-> ")
                print('-' * 10)
                
                self._student.design_proker(proker, self._bem)
                print('=' * 35)

            # Jika user memilih menjalankan tugas, tampilkan proker yang tersedia dan meminta input dari user untuk memilih proker yang akan dijalankan oleh member
            elif choice == 3:
                self._bem.displayProkers()

                print('=' * 35)
                print("Masukan nomor Proker:")
                proker = int(input("-> "))
                print('-' * 10)

                self._student.execute_proker(self._bem.get_proker(proker-1), self._bem)
                print('=' * 35)

            # Jika user memilih ikuti evaluasi, member akan mengikuti evaluasi
            elif choice == 4:
                self._student.attend_evaluation()
                print('=' * 35)

    def EnglishClubSimulation(self):

        while True:
            # Menampilkan pilihan untuk memilih aksi untuk member yang dipilih
            print(f"Hallo {self._student.getName()}, selamat datang di EnglishClub")
            print('-' * 35)
            print("Apa yang ingin kamu lakukan hari ini?")
            print("1. Menampilkan Proker")
            print("2. Merancang Proker")
            print("3. Belajar bahasa inggris")
            print("0. Exit")
            print('=' * 35)

            choice = int(input("-> "))
            print('-' * 10)

            if choice == 0:
                break

            elif choice == 1:
                self._englishClub.displayProkers()
                print('=' * 35)

            elif choice == 2:
                print("Masukan nama Proker:")
                proker = input("-> ")
                print('-' * 10)
                
                self._student.design_proker(proker, self._englishClub)
                print('=' * 35)

            elif choice == 3:
                self._student.learn_english()
                print('=' * 35)

        print("Do you want to go to the leader election? (y/n)")
        choice = input("-> ")
        print('-' * 10)
        if choice.lower() == "y":
            print("English Club Member are preparing for the election.")
            self._englishClub.selectLeader()
            print('=' * 35)


    def AssistantSimulation(self):
        
        while True:
            # Menampilkan pilihan untuk memilih aksi untuk member yang dipilih
            print(f"Hallo {self._student.getName()}")
            print('-' * 35)
            print("Apa yang ingin Anda lakukan hari ini?")
            print("1. Mengajar")
            print("2. Memberi tugas")
            print("0. Exit")
            print('=' * 35)

            choice = int(input("-> "))
            print('-' * 10)

            if choice == 0:
                break

            elif choice == 1:
                print("Masukan Subject:")
                subject = input("-> ")
                print('-' * 10)
                
                self._student.teach(subject)
                print('=' * 35)

            elif choice == 2:
                print("Masukan Tugas:")
                task = input("-> ")
                print('-' * 10)

                # call method on assistant class
                self._student.giveAssignment(task, self._students)
                print('=' * 35)

    def lecturerSimulation(self):

        while True:
            # Menampilkan pilihan untuk memilih aksi untuk member yang dipilih
            print(f"Hallo {self._lecturer.getName()}")
            print('-' * 35)
            print("Apa yang ingin Anda lakukan hari ini?")
            print("1. Mengajar")
            print("2. Memberi tugas")
            print("3. Memberi Nilai")
            print("0. Exit")
            print('=' * 35)

            choice = int(input("-> "))
            print('-' * 10)

            if choice == 0:
                break

            elif choice == 1:
                print("Masukan Subject:")
                subject = input("-> ")
                print('-' * 10)
                
                self._lecturer.teach(subject)
                print('=' * 35)

            elif choice == 2:
                print("Masukan Tugas:")
                task = input("-> ")
                print('-' * 10)

                # call method on assistant class
                self._lecturer.giveAssignment(task, self._students)
                print('=' * 35)

            elif choice == 3:
                # print the list of students
                print("List of Students:")
                for i, student in enumerate(self._students):
                    print(f"{i+1}. {student.getName()}")
                print('=' * 35)

                # ask user to choose a student
                print("Pilih Mahasiswa yang akan diberi nilai:")
                choice = int(input("-> "))
                print('-' * 10)

                # find the chosen student in the list of students
                student = None
                if choice < len(self._students):
                    student = self._students[choice-1]
                else:
                    print("Index out of range.")
                    continue

                print("Masukan Nilai:")
                score = int(input("-> "))
                print('-' * 10)

                self._lecturer.giveScore(score, student)
    
    def choiceStudent(self):

        def getYesOrNot(who):
            # notify
            print(f"This student is a {who} member.")
            print('=' * 35)

            # ask if the user wants to continue with the BEM simulation
            print(f"Do you want to continue with the {who} simulation? (y/n)")
            choice = input("-> ")
            print('-' * 10)
            return choice

        while True:
            # print the list of students
            print("List of Students:")
            for i, student in enumerate(self._students):
                print(f"{i+1}. {student.getName()}")
            print("0. Exit.")
            print('=' * 35)

            # ask user to choose a student
            choice = int(input("-> "))
            print('-' * 10)

            # Jika user memilih keluar, keluar dari loop while
            if choice == 0:
                break

            # find the chosen student in the list of students
            self._student = None
            if choice <= len(self._students):
                self._student = self._students[choice-1]
            else:
                print("Index out of range.")
                continue

            # print the student's information
            print("Student Information:")
            self._student.displayAll()
            print('-' * 10)
            
            # check if the student is a BEM member or an EnglishClub member
            if isinstance(self._student, BEMMember):
                choice = getYesOrNot("BEM")
                if choice.lower() == "y":
                    # continue with the BEM simulation
                    self.BEMSimulation()

            elif isinstance(self._student, EnglishClubMember):
                choice = getYesOrNot("English Club")
                if choice.lower() == "y":
                    # continue with the EnglishClub simulation
                    self.EnglishClubSimulation()

            elif isinstance(self._student, Assistant):
                choice = getYesOrNot("Assistant")
                if choice.lower() == "y":
                    # continue with the Assistant simulation
                    self.AssistantSimulation()

            else:
                print("This student is not a member of any organization.")
                print('=' * 40)

    def choiceLecturer(self):

        while True:
            # print the list of lecturers
            print("List of Lecturer:")
            for i, lecturer in enumerate(self._lecturers):
                print(f"{i+1}. {lecturer.getName()}")
            print("0. Exit.")
            print('=' * 35)

            # ask user to choose a lecturer
            choice = int(input("-> "))
            print('-' * 10)

            # Jika user memilih keluar, keluar dari loop while
            if choice == 0:
                break

            # find the chosen lecturer in the list of lecturers
            self._lecturer = None
            if choice <= len(self._lecturers):
                self._lecturer = self._lecturers[choice-1]
            else:
                print("Index out of range.")
                continue

            # show information lecturer
            print("Lecturer information:")
            self._lecturer.displayAll()
            print("-" * 10)

            # go to simulation
            self.lecturerSimulation()

    def choiceStart(self):

        while True:
            # display menu for choice
            print("Choice:")
            print("1. Mahasiswa")
            print("2. Dosen")
            print("0. Exit")
            print('=' * 35)

            # input choice
            choice = int(input("-> "))
            print('-' * 10)

            # menjalankan sistem yang sudah dipilih
            if choice == 0:
                break

            elif choice == 1:
                self.choiceStudent()

            elif choice == 2:
                self.choiceLecturer()

            else:
                print("Invalid choice.")