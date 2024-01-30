#Potęgowanie
try:
    podstawa = float(input("Wpisz podstawę potęgi: "))
    wykladnik = float(input("Wpisz wykladnik potegi: "))
except ValueError:
    print("Błąd zmiennej")
print("Wynik działania to: ",podstawa**wykladnik)