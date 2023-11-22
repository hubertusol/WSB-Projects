class Prostokat:
    def __init__(self,dlugosc,szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    def czy_kwadrat(self):
        if self.dlugosc==self.szerokosc:
            return True
        else:
            return False
figura1 = Prostokat(25,25)
figura2 = Prostokat(10,12)
print(figura1.czy_kwadrat())
print(figura2.czy_kwadrat())

