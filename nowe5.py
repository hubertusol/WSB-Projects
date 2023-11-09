import PySimpleGUI as sg
lista=[]
def zamien_na_liste(tekst):
    liczba = ''
    for x in range(0, len(tekst)):
        if tekst[x] != "," and tekst[x] != " ":
            liczba += tekst[x]
        if tekst[x] == "," or x+1 == len(tekst):
            try:
                liczba = int(liczba)
                lista.append(liczba)
            except ValueError:
                continue
            liczba = ''  # Resetuj zmienną liczba po dodaniu do listy
def dodaj_liczby(mylist):
    wynik=0
    for x in mylist:
        wynik+=x
    return wynik
layout = [
    [sg.Text("Prosze wpisac liczby oddzielone przecinkami: "),sg.InputText(key='-input-')],
    [sg.Button("Oblicz"),sg.Button("Wyjdz")]
]
window = sg.Window("Suma liczb",layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Wyjdz":
        break
    if event == "Oblicz":
        zamien_na_liste(values['-input-'])
        print("wynik: ",dodaj_liczby(lista))