szavak = ["alma", "cseresznye", "körte", "dió", "görögdinnye", "eper"]

szurt_es_nagybetus = [szo.upper() for szo in szavak if len(szo) <= 5]

print(szurt_es_nagybetus)


import random

idezetek = [
    "A kódolás olyan, mint a humor. Ha magyarázni kell, akkor rossz.",
    "A hibák nem a programozó ellenségei, hanem a tanítói.",
    "Először oldd meg a problémát. Aztán írd meg a kódot.",
    "Minden szoftver addig jó, amíg nem próbálod meg használni.",
    "A tiszta kód mindig úgy néz ki, mintha valaki olyan írta volna, akit érdekelsz.",
    "A számítógépek gyorsak, de buták. Az emberek lassúak, de okosak."
]

def napi_idezet(lista):
    while True:
        yield random.choice(lista)


idezet_generator = napi_idezet(idezetek)

print("--- Tesztelés a next() függvénnyel ---")
print("1.", next(idezet_generator))
print("2.", next(idezet_generator))

print("\n--- Tesztelés for ciklussal (5 alkalommal) ---")

for i in range(5):
    print(f"{i + 3}.", next(idezet_generator))


szamok = [-5, 3, 0, -12, 8, 2, -1]

tizszeres_generator = (szam * 10 for szam in szamok if szam > 0)

print("A pozitív számok tízszerese:")
for ertek in tizszeres_generator:
    print(ertek)




szavak = ["BANÁN", "fa", "CSERESZNYE", "ő", "Szilva", "tó", "BORS"]


kisbetus_szavak = list(map(lambda szo: szo.lower(), szavak))

szurt_szavak = list(filter(lambda szo: len(szo) >= 3, kisbetus_szavak))

print("Eredeti szavak:", szavak)
print("Kisbetűsítve:  ", kisbetus_szavak)
print("Végeredmény:   ", szurt_szavak)