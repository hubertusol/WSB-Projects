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
class Student(Osoba):
    def __init__(self, imie, wiek,oceny):
        super().__init__(imie, wiek)
        self.oceny=oceny
    def srednia(self):
        if not self.oceny:
            return 0
        suma=0
        for ocena in self.oceny:
            suma+=ocena
        srednia_ocen=suma/len(self.oceny)
        return srednia_ocen
oceny_studenta = [4.5,4,3,5]
student = Student("Hubert",20,oceny_studenta)
print(f"Średnia ocen studenta {student.imie}: {student.srednia()}")