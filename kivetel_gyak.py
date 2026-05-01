def biztonsagos_input(prompt="Kérek egy számot: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Hiba: Nem számot adott meg! Próbáld újra.")

def szam_atlag(lista):
    if not lista:
        raise ValueError("A lista üres!")
    osszeg = 0
    for elem in lista:
        if not isinstance(elem, (int, float)):
            raise TypeError(f"Nem szám típus: {elem}")
        osszeg += elem
    return osszeg / len(lista)

def main():
    try:
        fajlnev = input("Adj meg egy fájlnevet: ")
        f = open(fajlnev, "r", encoding="utf-8")
        tartalom = f.read()
        print("A fájl tartalma:")
        print(tartalom)
        f.close()
    except FileNotFoundError:
        print("Hiba: A fájl nem létezik!")
    finally:
        print("A fájlművelet véget ért.")


if __name__ == "__main__":
    print("Teszt: helyes lista [1, 2, 3, 4]")
    print(szam_atlag([1, 2, 3, 4]))  # 2.5
    print("Teszt: hibás lista [1, 'a', 3]")
    try:
        print(szam_atlag([1, 'a', 3]))
    except Exception as e:
        print(f"Kivétel: {e}")
    print("Teszt: üres lista []")
    try:
        print(szam_atlag([]))
    except Exception as e:
        print(f"Kivétel: {e}")

    # Biztonságos input teszt
    print("Biztonságos input teszt: (adj meg egy számot, majd próbálj hibásat is)")
    szam = biztonsagos_input()
    print(f"A megadott szám: {szam}")

