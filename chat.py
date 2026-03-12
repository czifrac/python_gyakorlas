def feldolgozas(kerdes):
    print("feldolgozas alatt: " + kerdes)


    if kerdes.endswith("?"):
        print("Ez bizony egy kérdés")

    szamjegyek = dict()
    for betu in kerdes:
        if betu in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if betu in szamjegyek:
                szamjegyek[betu] += 1
            else:
                szamjegyek[betu] = 1

    if not szamjegyek:
        print("Ebben egy számjegy sem volt.")


    pontok_szama = kerdes.count(".")
    print(f"A kérdés {pontok_szama} darab pontot tartalmazott.")

    return szamjegyek


while True:
    kerdes = input("Kerdes: ")


    if kerdes == "exit" or kerdes == "quit":
        print("Bye!")
        break

    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)

    print("Válasz: " + str(valasz))


print("VEGE.")