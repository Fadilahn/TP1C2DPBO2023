class Proker:
    _prokers = []

    def __init__(self):
        pass

    # method untuk menambahkan proker baru
    def add_proker(self, proker):
        if isinstance(proker, list):
            self._prokers.extend(proker)
        else:
            self._prokers.append(proker)

    # method untuk mendapatkan prokerdengan indeks tertentu
    def get_proker(self, proker):
        if isinstance(proker, int):
            return self._prokers[proker]
        elif isinstance(proker, str):
            for i in self._prokers:
                if i == proker:
                    return i
        else:
            print("Error")

    # method untuk menghapus proker dari daftar proker
    def remove_proker(self, proker):
        if not proker:
            self._prokers = []
        elif isinstance(proker, int):
            del self._prokers[proker]
        elif isinstance(proker, str):
            self._prokers.remove(proker)
        else:
            print("Error")

    # method untuk menampilkan daftar proker
    def displayProkers(self):
        for i, proker in enumerate(self._prokers):
            print(f"{i+1}. {proker}")
 