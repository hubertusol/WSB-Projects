import PySimpleGUI as sg
def zamien_na_liste(tekst):
    liczba = ''
    lista =[]
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
    return lista
def policz_potegi(mylist):
    wynik = []
    for x in mylist:
        wynik.append(x*x)
    return wynik
layout = [
    [sg.Text("Wpisz listę liczb, odzielonych przecinkami "),sg.InputText(key='-input-')],
    [sg.Button("Oblicz"),sg.Button("Wyjdz")],
    [sg.Text(" ",key='-output-')]
]
window = sg.Window("Potegi",layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Wyjdz":
        break
    if event == "Oblicz":
        policzona_lista = zamien_na_liste(values['-input-'])
        policz_potegi(policzona_lista)
        window['-output-'].update(policz_potegi(policzona_lista))