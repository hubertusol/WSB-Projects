#Analiza tekstu

from ast import And


tekst = input("Wprowadź swój tekst: ")
ciag=tekst.lower().replace(' ','')
slowa=1
for i in range(0, len(tekst)):
    print(i, tekst[i])
    #program liczy ilość słów dzięki ilości spacji
    if tekst[i] == ' ' and i+1<len(tekst) and tekst[i+1]!=' ':
        #instrukcja warunkowa sprawdza czy uzytkownik nie wpisal paru spacji pod rzad albo spacji na koncu
        slowa+=1
print("Liczba liter: ",len(ciag))
print("Liczba slow: ",slowa)
