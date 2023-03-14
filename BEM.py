from Student import Student

# define BEMMember class
class BEMMember(Student):
    # deklarasi atribut
    _evaluated = True

    # constructor, memanggil constructor superclass Student dan menambahkan atribut _evaluated
    def init(self, name, gender, nim):
        super().init(name, gender, nim)
        self._evaluated = True

    # method untuk merancang proker
    def design_proker(self, proker, bem):
        # memeriksa apakah anggota sudah dievaluasi atau belum, jika sudah berhasil menambahkan proker
        if self._evaluated:
            bem.add_proker(proker)
            print("Succeed ^-^")
            print(f"Proker {proker} berhasil dirancang dan ditambahkan ke list proker BEM")
        else:
            print("Failed T_T")
            print("Anda harus menghadiri evaluasi terlebih dahulu untuk dapat merancang proker")

    # method untuk melaksanakan proker
    def execute_proker(self, proker, bem):
        # memeriksa apakah anggota sudah dievaluasi atau belum, jika sudah berhasil menghapus proker
        if self._evaluated:
            bem.remove_proker(proker)
            print("Succeed ^-^")
            print(f"Proker {proker} telah dilaksanakan")
            self._evaluated = False
        else:
            print("Failed T_T")
            print("Anda harus menghadiri evaluasi terlebih dahulu untuk dapat melaksanakan proker")

    # method untuk menghadiri evaluasi
    def attend_evaluation(self):
        # memeriksa apakah anggota sudah dievaluasi atau belum, jika belum berhasil mengubah status evaluated
        if self._evaluated:
            print("Failed T_T")
            print("Anda belum dapat menghadiri evaluasi, karena masih ada proker yang perlu dilaksanakan")
        else:
            self._evaluated = True
            print("Succeed ^-^")
            print("Anda berhasil menghadiri evaluasi")

# define BEM class
class BEM:
    _name = "" # variabel untuk menyimpan nama BEM
    _members = [] # variabel untuk menyimpan daftar member BEM
    _prokers = [] # variabel untuk menyimpan daftar proker BEM

    # method konstruktor, digunakan saat membuat objek BEM baru
    def __init__(self, name):
        self._name = name

    # method untuk mendapatkan nama BEM
    def getName(self):
        return self._name

    # method untuk menambahkan member baru ke dalam BEM
    def add_member(self, member):
        if isinstance(member, BEMMember):
            self._members.append(member)

    # method untuk mendapatkan member BEM dengan indeks tertentu
    def get_member(self, member):
        if isinstance(member, int):
            return self._members[member]
        elif isinstance(member, str):
            for i in self._members:
                if i == member:
                    return i
        else:
            print("Error")

    # method untuk menambahkan proker baru ke dalam BEM
    def add_proker(self, proker):
        if isinstance(proker, list):
            self._prokers.extend(proker)
        else:
            self._prokers.append(proker)

    # method untuk mendapatkan proker BEM dengan indeks tertentu
    def get_proker(self, proker):
        if isinstance(proker, int):
            return self._prokers[proker]
        elif isinstance(proker, str):
            for i in self._prokers:
                if i == proker:
                    return i
        else:
            print("Error")

    # method untuk menghapus proker dari daftar proker BEM
    def remove_proker(self, proker):
        if not proker:
            self._prokers = []
        elif isinstance(proker, int):
            del self._prokers[proker]
        elif isinstance(proker, str):
            self._prokers.remove(proker)
        else:
            print("Error")

    # method untuk menampilkan daftar proker BEM
    def displayProkers(self):
        print(f"Proker BEM {self._name}:")
        for i, proker in enumerate(self._prokers):
            print(f"{i+1}. {proker}")

    # method untuk menampilkan daftar member BEM
    def displayMember(self):
        print(f"Member BEM {self._name}:")
        for i, member in enumerate(self._members):
            print(f"{i+1}. {member.getName()}")