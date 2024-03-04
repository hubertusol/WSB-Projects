while True:
    print("1) Stworz nowy plik")
    print("2) Wyswietl plik")
    print("3) Dodaj tekst do pliku")
    try: wybor =int(input("Wybierz 1 2 lub 3: "))
    except ValueError:
        print("Błąd: Musisz wybrac liczbe")
        continue
    if wybor not in range(1,4):
        print("Błąd: Liczba musi byc w zakresie 1-3")
        continue
    if wybor==1:
        file = open("d:/WSB-Projects/OB-Python-Lubicka/Subject.txt",'w')
        file.close()
    if wybor==2:
        file = open("d:/WSB-Projects/OB-Python-Lubicka/Subject.txt",'r')
        print(file.readlines())
        file.close()
    if wybor==3:
        file = open("d:/WSB-Projects/OB-Python-Lubicka/Subject.txt",'a')
        subject = str(input("Prosze wpisac tekst do dodania: "))
        file.write(f"{subject}\n")
        file.close()