
numbers = [int(x) for x in input("Podaj listę liczb oddzielonych spacjami: ").split()]
search_num = int(input("Podaj liczbę do sprawdzenia: "))
if search_num in numbers:
    print(f"Liczba {search_num} znajduje się na liście.")
else:
    print(f"Liczba {search_num} nie znajduje się na liście.")
