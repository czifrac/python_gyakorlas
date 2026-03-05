
def feldolgozas(kerdes):
    print("feldolgozas alatt: " + kerdes)


    szamjegyek = dict()
    for betu in kerdes:
        print(betu)




while True:
    kerdes = input("Kerdes: ")

    if kerdes == "exit":
        print("Bye!")
        break

    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)

    print("Válasz: " + str(valasz))


print("VEGE.")