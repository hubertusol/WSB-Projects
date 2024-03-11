a = input("Prosze wpisac posortowane liczby oddzielone spacjami: ").split()
n=len(a)
b = int(input("Prosze wpisac zmienna b: "))
wynik=0
for number in a:
    if int(number)<=b: 
        wynik+=1
print(wynik)