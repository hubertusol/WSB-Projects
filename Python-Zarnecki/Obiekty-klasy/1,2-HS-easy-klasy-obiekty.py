class Osoba:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek=wiek
    def przedstaw_sie(self):
        print("Jestem "+self.imie+" i mam "+str(self.wiek)+" lat")
osoba1 = Osoba("Anna",25)
osoba2 = Osoba("Tomasz",30)
print(f"Osoba 1: {osoba1.imie}, {osoba1.wiek} lat")
print(f"Osoba 2: {osoba2.imie}, {osoba2.wiek} lat")
osoba1.przedstaw_sie()
osoba2.przedstaw_sie()