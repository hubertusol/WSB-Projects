class Ksiazka:
    def __init__(self,tytul,autor,strony):
        self.tytul = tytul
        self.autor = autor
        self.strony = strony
    def opis(self):
        print(self.tytul,self.autor,self.strony,sep="\n")
Das_Kapital = Ksiazka("Das Kapital","Karl Marx",70)
Das_Kapital.opis()