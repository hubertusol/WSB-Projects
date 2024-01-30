liczba = int(input("Prosze wpisac liczbę: "))
for x in range(1,liczba):
    lista_dzielnikow = []
    suma_dzielnikow = 0
    for i in range(1,x):
        if x%i==0:
            lista_dzielnikow.append(i)
        suma_dzielnikow=sum(lista_dzielnikow)
    if suma_dzielnikow==x: print(f"Liczba Doskonała: {x}")
