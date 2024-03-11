# Importujemy moduł os, aby móc przeglądać pliki w katalogu
import os

# Funkcja do przeczytania zawartości programów i zapisania ich do pliku tekstowego
def zapisz_programy_do_pliku(nazwa_pliku_wyjsciowego):
    # Otwieramy plik wyjściowy w trybie zapisu tekstowego
    with open(nazwa_pliku_wyjsciowego, 'w') as plik_wyjsciowy:
        # Iterujemy po numerach programów od 105 do 113
        for numer_programu in range(105, 114):
            nazwa_pliku = f"{numer_programu}.py"
            # Sprawdzamy, czy plik istnieje
            if os.path.exists(nazwa_pliku):
                # Jeśli istnieje, otwieramy go i odczytujemy zawartość
                with open(f"d:/WSB-Projects/OB-Python-Lubicka/{nazwa_pliku}", 'r') as plik:
                    zawartosc = plik.read()
                # Zapisujemy opis programu w komentarzu oraz jego zawartość do pliku tekstowego
                plik_wyjsciowy.write(f"# Program {numer_programu}\n")
                plik_wyjsciowy.write(zawartosc)
                plik_wyjsciowy.write("\n\n")

# Wywołujemy funkcję, aby zapisać programy do pliku tekstowego 'text.txt'
zapisz_programy_do_pliku("text.txt")
