class Kalkulator:
    def __init__(self, wynik):
        self.wynik=wynik
    def dodaj(self,x):
        self.wynik+=x
        print(self.wynik)
    def odejmij(self,x):
        self.wynik-=x
        print(self.wynik)
    def pomnoz(self,x):
        self.wynik*=x
        print(self.wynik)
    def podziel(self,x):
        self.wynik/=x
        print(self.wynik)
wartosci = Kalkulator(80)
wartosci.dodaj(10)
wartosci.odejmij(30)
wartosci.pomnoz(2)
wartosci.podziel(3)
