print("hello")

# ez egy komment

"""
többsoros
komment
"""

x = 10
print(x)

nev = "Valaki"
print(nev)

print([1, 2, 3, 4, 5])

print(range(5))

szotar = {"név": "Anna", "kor": 20}
print(szotar)
logikai = True
print(logikai)

ertek = None
print(ertek)

PI = 3.14
print(PI)

x = 5
y = 3
print("x mod y: " + str(x % y))

if y > 5:
    print("y nagyobb mint 5")
    if y % 2 == 0:
        print("y páros és nagyobb mint 5")

else:
    print("y kisebb vagy egyenlő mint 5")

for i in range(5):
        print(i)

def osszead(a, b):
    osszeg = a + b
    return osszeg


