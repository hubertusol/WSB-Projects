#Głosowanie
try:
    wiek = int(input("Wpisz swoj wiek: "))
except ValueError:
    print("Błąd zmiennej")
if wiek>=18:
    print("Możesz głosować")
else:
    print("Nie możesz głosować")