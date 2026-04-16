class Dokumentum:
    def __init__(self, cim):
        self.cim = cim


class Film(Dokumentum):
    def __init__(self, cim, rendezo, ev):
        super().__init__(cim)
        self.rendezo = rendezo
        self.ev = ev

    def leiras(self):
        print(f"{self.rendezo} - {self.cim}")

    def regi_e(self):
        return self.ev < 2000


class Konyv(Dokumentum):
    def __init__(self, cim, szerzo, oldalszam):
        super().__init__(cim)
        self.szerzo = szerzo
        self.oldalszam = oldalszam

    def hosszu_e(self):
        return self.oldalszam > 300

    def leiras(self):
        print(f"Könyv: {self.szerzo} - {self.cim}, {self.oldalszam} oldal")


class Folyoirat(Dokumentum):
    def __init__(self, cim, evfolyam, szam):
        super().__init__(cim)
        self.evfolyam = evfolyam
        self.szam = szam

    def leiras(self):
        print(f"Folyóirat: {self.cim}, {self.evfolyam}. évfolyam, {self.szam}. szám")
