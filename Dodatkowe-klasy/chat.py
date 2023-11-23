class Gra:
    def __init__(self, tytul, gatunek, ocena):
        self.tytul = tytul
        self.gatunek = gatunek
        self.ocena = ocena

class Biblioteka:
    def __init__(self):
        self.lista_gier = []

    def dodaj_gre(self, gra):
        if isinstance(gra, Gra):
            self.lista_gier.append(gra)
            print(f"Dodano grę '{gra.tytul}' do biblioteki.")
        else:
            print("Podany obiekt nie jest instancją klasy Gra.")

    def usun_gre(self, tytul):
        for gra in self.lista_gier:
            if gra.tytul == tytul:
                self.lista_gier.remove(gra)
                print(f"Usunięto grę '{gra.tytul}' z biblioteki.")
                return
        print(f"Nie znaleziono gry o tytule '{tytul}'.")

    def wyszukaj_gre(self, gatunek):
        znalezione_gry = [gra for gra in self.lista_gier if gra.gatunek == gatunek]
        if znalezione_gry:
            print(f"Gry z gatunku '{gatunek}':")
            for gra in znalezione_gry:
                print(f"Tytuł: {gra.tytul}, Ocena: {gra.ocena}")
        else:
            print(f"Brak gier z gatunku '{gatunek}'.")

# Prosty program wykorzystujący klasy do zarządzania kolekcją gier użytkownika
moja_biblioteka = Biblioteka()

while True:
    print("\n===== MENU =====")
    print("1. Dodaj grę")
    print("2. Usuń grę")
    print("3. Wyszukaj grę po gatunku")
    print("4. Wyjście")
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        tytul = input("Podaj tytuł gry: ")
        gatunek = input("Podaj gatunek gry: ")
        ocena = input("Podaj ocenę gry: ")
        nowa_gra = Gra(tytul, gatunek, ocena)
        moja_biblioteka.dodaj_gre(nowa_gra)
    elif wybor == "2":
        tytul_do_usuniecia = input("Podaj tytuł gry do usunięcia: ")
        moja_biblioteka.usun_gre(tytul_do_usuniecia)
    elif wybor == "3":
        gatunek_do_wyszukania = input("Podaj gatunek do wyszukania: ")
        moja_biblioteka.wyszukaj_gre(gatunek_do_wyszukania)
    elif wybor == "4":
        print("Dziękujemy! Do widzenia.")
        break
    else:
        print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")
