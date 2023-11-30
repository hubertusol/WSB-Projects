try: 
    liczba=int(input("Prosze wpisac liczbe: "))
    if liczba%2==0: print("Liczba jest parzysta")
    else: print("Liczba jest nieparzysta")
except ValueError: print("Wpisz poprawna liczbe!")
