import csv
file = open("d:/WSB-Projects/OB-Python-Lubicka/Books.csv","a")
name = input("Wpisz nazwę ksiazki: ")
author = input("Wpisz imie i nazwisko autora: ")
year = input("Wpisz rok wydania: ")
file.write("\n")
file.write(f"{name},{author},{year}")
file.close()
file = open("d:/WSB-Projects/OB-Python-Lubicka/Books.csv","r")
for record in file:
    print(record,end="")