class Konyvtar:
    def __init__(self):
        self.konyvek = []

    def konyv_hozzaadasa(self, konyv):
        self.konyvek.append(konyv)

    def listazas(self):
        for konyv in self.konyvek:
            konyv.leiras()
