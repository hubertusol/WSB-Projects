class Gra:
    def __init__(self,tytuł,gatunek,ocena):
        self.tytuł=tytuł
        self.gatunek=gatunek
        self.ocena=ocena
class Biblioteka:
    def __init__(self):
        self.lista_gier=[]
    def dodaj_gre(self,gra):
        if isinstance(gra,Gra):
            self.lista_gier.append(gra)
    def usun_gre(self,gra):
        self.lista_gier.remove(gra)
    def znajdz_gre(self,nazwa_gry):
        find=False
        for i,value in enumerate(self.lista_gier,start=1):
            if value.tytuł==nazwa_gry:
                find=True
                print("Znaleziono gre w bibliotece")
                print(f"{value} znajduje się na {i} miejscu w liscie")
        if find==False: print("Gra nie znajduje sie w bibliotece")

#program do zarządzania biblioteką
moja_biblioteka=Biblioteka()
while True:
    print("Wpisz polecenie lub ? aby otrzymać listę poleceń")
    polecenie = input("#> ")
    if polecenie=="?":
        print("""
        wartości wpisz w cudzysłowiach " "
        #>dodaj <nazwa gry> <gatunek> <ocena> -> dodaje grę
        #>usun <nazwa gry> -> usuwa grę o podanej nazwie
        #>szukaj <gatunek> -> szukaj wszystkie gry z gatunku
        """)
    elif polecenie.startswith("dodaj"):
        polecenie.split() #do dokonczenia