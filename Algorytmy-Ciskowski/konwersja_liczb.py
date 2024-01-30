#ĆW.01. Zadanie 4
try:
    x = int(input("Proszę wpisać liczbę dziesiętną do konwersji: "))
    y = int(input("Proszę wpisać podstawę systemu liczbowego (2-36): "))
    if y not in range(2,37):
        print("Proszę wpisac podstawę w zakresie 2-36")
        exit()
except ValueError: 
    print("Prosze wpisac liczbę całkowitą")
    exit()
wynik=[]
def zamien(zmienna, podstawa):
    if zmienna!=0:
        reszta=zmienna%podstawa
        zmienna=zmienna//podstawa
        if reszta in range(0,10):
            wynik.insert(0,reszta) 
        else:
            wynik.insert(0,chr(55+reszta)) #konwersja liczby na ASCII, gdy liczba jest większa od 9, (począwszy od A)
        zamien(zmienna,podstawa)
zamien(x,y)
for i in wynik: print(i,end='') #wyświetlenie listy w postaci stringa