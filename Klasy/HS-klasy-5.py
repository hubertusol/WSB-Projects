class Samochod:
    def __init__(self,marka,model,kolor,predkosc):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.predkosc = predkosc
    def przyspiesz(self):
        self.predkosc +=  30
        return self.predkosc
    def zwolnij(self):
        self.predkosc-=20
        return self.predkosc
auto = Samochod('Hyundai','i30','Szary',60)
print(f"Predkosc auta: {auto.predkosc} km/h")
print(f"Przyśpieszyłem! Aktualna predkośc: {auto.przyspiesz()} km/h")
print(f"Zwolniłem! Aktualna prędkość: {auto.zwolnij()} km/h")