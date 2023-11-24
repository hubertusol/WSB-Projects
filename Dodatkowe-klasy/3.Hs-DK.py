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
    def usun_gre(self,tytul_gry):
        removed=False
        for gra in self.lista_gier:
            if gra.tytuł==tytul_gry:
                self.lista_gier.remove(gra)
                print(f"{gra.tytuł} została usunięta z biblioteki")
                removed=True
            if removed==False: print("Nie ma takiej gry w bibliotece")
    def znajdz_gre(self,wartosc_szukana,parametr):
        find=False
        if parametr=="t"or parametr=="g" or parametr=="o":
            if parametr=="o": 
                try: wartosc_szukana=int(wartosc_szukana)
                except: print("prosze wpisac ocene w formie numeru 1-10")
            if parametr=="t":
                for i,value in enumerate(self.lista_gier,start=1):
                    if value.tytuł==wartosc_szukana:
                        find=True
                        print(f"{i}. Tytuł: '{value.tytuł}' Gatunek: '{value.gatunek}' Ocena: '{value.ocena}'")
                if find==False: print("Gra nie znajduje sie w bibliotece")
            elif parametr=="g":
                for i,value in enumerate(self.lista_gier,start=1):
                    if value.gatunek==wartosc_szukana:
                        find=True
                        print(f"{i}. Tytuł: '{value.tytuł}' Gatunek: '{value.gatunek}' Ocena: '{value.ocena}'")
                if find==False: print("Gra nie znajduje sie w bibliotece")
            elif parametr=="o":
                for i,value in enumerate(self.lista_gier,start=1):
                    if value.ocena==wartosc_szukana:
                        find=True
                        print(f"{i}. Tytuł: '{value.tytuł}' Gatunek: '{value.gatunek}' Ocena: '{value.ocena}'")
                if find==False: print("Gra nie znajduje sie w bibliotece")
        else: print("Błędny parametr.")
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
        #>szukaj -t/-g/-o <wartosc> -> szukaj gry za pomoca tytulu/gatunku/oceny
        #>wyjdz - wychodzi z programu
        """)
    elif polecenie.startswith("dodaj"):
        try:
            nazwa = polecenie.split('"')[1]
            gatunek = polecenie.split('"')[3]
            ocena = int(polecenie.split('"')[5])
            gra_do_dodania = Gra(nazwa,gatunek,ocena)
            moja_biblioteka.dodaj_gre(gra_do_dodania)
            print("Gra pomyslnie dodana!")
        except: print("Błąd, prosze spróbowac jeszcze raz")
    elif polecenie.startswith("szukaj"):
        litera = polecenie[8]
        wartosc_szukanie = polecenie.split('"')[1]
        moja_biblioteka.znajdz_gre(wartosc_szukanie,litera)
    elif polecenie.startswith("usun"):
        gra_usuwanie = polecenie.split('"')[1]
        moja_biblioteka.usun_gre(gra_usuwanie)
    elif polecenie.startswith("wyjdz"):
        print("Dziekuje, do widzenia")
        break
    else: print("Prosze wpisac poprawna komende")