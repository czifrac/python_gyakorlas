def szam_generator():
    for szam in range(1, 6):
        yield szam


def paros_generator():
    for szam in range(0, 11, 2):
        yield szam

negyzet = lambda x: x ** 2
print(negyzet(4))

paratlan_harom = [x * 3 for x in range(1, 11) if x % 2 == 1]
print(paratlan_harom)

lista = [10, 15, 20, 25]
# Mindet megszorozzuk 3-mal
szorozva = list(map(lambda x: x * 3, lista))
print(szorozva)  # [30, 45, 60, 75]
# Csak a 20 felettiek
husz_felett = list(filter(lambda x: x > 20, lista))
print(husz_felett)  # [25]
