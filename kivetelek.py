try:

    eletkor_str = input("Kérlek, add meg az életkorodat: ")


    eletkor = int(eletkor_str)


    hatralevo_evek = 100 - eletkor


    print(f"Még {hatralevo_evek} év múlva leszel 100 éves.")

except ValueError:

    print("Hiba: Nem számot adtál meg! Kérlek, számjegyekkel add meg az életkorod.")

fajlnev = input("Kérlek, add meg a fájlnevet (pl. adatok.txt): ")

try:

    with open(fajlnev, 'r', encoding='utf-8') as fajl:

        elso_sor = fajl.readline().strip()

        try:

            szam = float(elso_sor)

            print(f"A fájl első sorában lévő szám kétszerese: {szam * 2}")

        except ValueError:
            print("A fájl első sora nem szám.")

except FileNotFoundError:
    print("Nincs ilyen fájl.")

try:
    jelszo = input("Kérlek, add meg a jelszót: ")

    if len(jelszo) < 8:
        raise Exception("A jelszó túl rövid! Legalább 8 karakter hosszúnak kell lennie.")

    print("Jelszó elfogadva.")

except Exception as e:
    print(f"Hiba: {e}")