import random
liczba = random.randint(1,100)
while True:
    try: proba = int(input("Prosze wpisac liczbe: "))
    except  ValueError:
         print("Prosze wpisac prawidłową liczbę!")
         continue
    if proba in range(1,100):
        if proba>liczba: print("Za duzo!")
        elif proba<liczba: print("Za mało!")
        elif proba==liczba: 
            print("Brawo! udalo ci sie zgadnac!")
            break
    else: print("Wpisz liczbe od 1 do 100")