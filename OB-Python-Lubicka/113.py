import csv
try: liczba = int(input("Prosze wybrac ilosc wierszy do dodania: "))
except ValueError:
    print("Musisz wpisac liczbe")
    exit
if liczba<1: exit
file = open("d:/WSB-Projects/OB-Python-Lubicka/Books.csv","a")
for i in range(0,liczba):
    name = input("Wpisz nazwę ksiazki: ")
    author = input("Wpisz imie i nazwisko autora: ")
    year = input("Wpisz rok wydania: ")
    file.write("\n")
    file.write(f"{name},{author},{year}")
file.close()
file = open("d:/WSB-Projects/OB-Python-Lubicka/Books.csv","r")
wybor = input("Prosze wybrac autora: ")
bol=False
for row in file:
    record = row.split(",")
    if wybor==record[1]:
        print(row)
        bol=True
if bol==False: print("Nie ma takiego autora w pliku")