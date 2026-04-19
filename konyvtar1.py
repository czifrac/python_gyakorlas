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

        eredmeny = "\n".join(str(konyv) for konyv in self.konyvek)
        return eredmeny

konyvtar = Konyvtar()
konyvtar.hozzaad("Egri csillagok", "Gárdonyi Géza")
konyvtar.hozzaad("1984", "George Orwell")

print(konyvtar)