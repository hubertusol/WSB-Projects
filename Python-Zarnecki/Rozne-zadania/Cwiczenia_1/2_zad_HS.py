Imie = input("Podaj swoje imie: \n")
try: 
    Rok = int(input("Podaj swoj rok urodzenia: \n"))
    if Rok<2023:
        Wiek = 2023-Rok
        print(f"{Imie}, masz {Wiek} lat.")
    else: print(f"{Imie}, masz mniej niż rok")
except: ValueError: print("Wpisz prosze liczbe")