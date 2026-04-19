
class Eloleny:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor


    def __str__(self):
        return f"Név: {self.nev}, Életkor: {self.eletkor} év"



class Noveny(Eloleny):
    def __init__(self, nev, eletkor, vizigeny):
        super().__init__(nev, eletkor)
        self.vizigeny = vizigeny

    def __str__(self):
        return f"[Növény] {super().__str__()}, Vízigény: {self.vizigeny}"


class Allat(Eloleny):
    def __init__(self, nev, eletkor, labak_szama):
        super().__init__(nev, eletkor)
        self.labak_szama = labak_szama

    def __str__(self):
        return f"[Állat] {super().__str__()}, Lábak száma: {self.labak_szama}"


class Gomba(Eloleny):
    def __init__(self, nev, eletkor, mergezo_e):
        super().__init__(nev, eletkor)
        self.mergezo_e = mergezo_e

    def __str__(self):

        mergezo_szoveg = "Igen" if self.mergezo_e else "Nem"
        return f"[Gomba] {super().__str__()}, Mérgező: {mergezo_szoveg}"



fikusz = Noveny(nev="Fikusz", eletkor=2, vizigeny="Közepes")
kutya = Allat(nev="Kutya", eletkor=5, labak_szama=4)
galoca = Gomba(nev="Gyilkos galóca", eletkor=0.1, mergezo_e=True)

print(fikusz)
print(kutya)
print(galoca)