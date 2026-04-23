class Konyv:
    def __init__(self, cim, szerzo):
        self.cim = cim
        self.szerzo = szerzo

    def __str__(self):
        return f"{self.cim} - {self.szerzo}"


class Konyvtar:
    def __init__(self):
        self.konyvek = []

    def hozzaad(self, cim, szerzo):
        uj_konyv = Konyv(cim, szerzo)
        self.konyvek.append(uj_konyv)

    def __str__(self):
        if not self.konyvek:
            return "A könyvtár jelenleg üres."
        return "\n".join(str(konyv) for konyv in self.konyvek)


    def __add__(self, masik_konyvtar):

        uj_konyvtar = Konyvtar()


        uj_konyvtar.konyvek = self.konyvek + masik_konyvtar.konyvek

        return uj_konyvtar


konyvtar1 = Konyvtar()
konyvtar1.hozzaad("Egri csillagok", "Gárdonyi Géza")
konyvtar1.hozzaad("1984", "George Orwell")

konyvtar2 = Konyvtar()
konyvtar2.hozzaad("A kis herceg", "Antoine de Saint-Exupéry")
konyvtar2.hozzaad("Dűne", "Frank Herbert")

uj_konyvtar = konyvtar1 + konyvtar2

print(uj_konyvtar)