dzialanie = input("Prosze wpisac działanie oddziel znaki spacjami, np 2 + 2: ")
try:
    a = dzialanie.split(" ")[0]
    znak = dzialanie.split(" ")[1]
    b = dzialanie.split(" ")[2]
except: print("Błąd")
class Kalkulator:
    def __init__(self,znak,x,y):
        self.znak=znak
        self.x=int(x)
        self.y=int(y)
    def wykonaj_dzialanie(self):
        if znak=="+": return self.x+self.y
        elif znak=="-": return self.x-self.y
        elif znak=="*": return self.x*self.y
        elif znak=="/": return self.x/self.y
        else: print("Niepoprawny znak")
obiekt = Kalkulator(znak,a,b)
print(obiekt.wykonaj_dzialanie())