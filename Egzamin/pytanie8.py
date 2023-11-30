def nwd(a, b):
    while a!= b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
def nww(a,b):
    return a * b // nwd(a,b)
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
print(f"Największy wspólny dzielnik liczb {a} i {b} wynosi",nwd(a, b))
print(f"Najwieksza wspolna wielokrotnosc liczb {a} i {b} wynosi",nww(a,b))