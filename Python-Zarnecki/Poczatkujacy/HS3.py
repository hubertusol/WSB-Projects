#Konwersja mil na kilometry
try: 
    mile = float(input("Wpisz liczbę mil: "))
    kilometry = float(input("Wpisz liczbę kilometrów: "))
except ValueError:
    print("Bład zmiennej")
print(mile," mile = ",mile/1.609," kilometrow")
print(kilometry, " kilometrow = ",kilometry*1.609," mil")