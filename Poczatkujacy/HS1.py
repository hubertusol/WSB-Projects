#ŚREDNIA
print("Program do liczenia średniej")
print("Możesz wpisać dowolną liczbę liczb całkowitych lub ułamków")
print("Aby zakończyć dodawanie numerów, wpisz literę")
lista= []
while True:
    try:
        liczba = float(input("Wpisz liczbę: "))
        lista.append(liczba)
    except ValueError:
        break
suma=0
for i in lista:
    suma+=i
print(suma/len(lista))