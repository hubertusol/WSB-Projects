#ĆW.01. Zadanie 3
#Hubert Sołtys
try:
    x = int(input("Proszę wpisać liczbę do zamiany na rzymską: "))
    if x<1:
        print("Liczba musi być większa od 0")
        exit()
except ValueError:
    print("Prosze wpisac liczbe calkowita")
    exit()
arabska=x
liczby_rzymskie = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
print(f"Liczba {x} zamieniona na zapis rzymski to: ",end='')
for rzymska,wartosc in liczby_rzymskie.items():
    while arabska>=wartosc:
        arabska-=wartosc
        print(rzymska,end='')