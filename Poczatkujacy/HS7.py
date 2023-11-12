#Gra w zgadywanie liczb
import random
losowa_liczba = random.randint(0,100)
proba=10
while proba>0:
    try:
        print("Pozostało ",proba," prób")
        liczba=int(input("Wpisz liczbę całkowitą: "))
        if liczba>losowa_liczba:
            print("Za dużo!")
        elif liczba<losowa_liczba:
            print("Za mało!")
        elif liczba==losowa_liczba:
            print("Brawo! Zgadłeś")
            break
        proba-=1
    except ValueError:
        print("Błąd zmiennej")
        continue
print("Koniec gry")