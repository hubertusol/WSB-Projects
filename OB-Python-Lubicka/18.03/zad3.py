text=input("Prosze wpisac ciag liczb sudoku: ")
lista_cyfr = list(text)
suma = 0
for number in lista_cyfr:
    try: suma+=int(number)
    except ValueError: pass
rozwiazanie=45-suma
print(rozwiazanie)