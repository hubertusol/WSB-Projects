import PySimpleGUI as sg

myList = []
layout = [
    [sg.Text("Proszę wpisać wartość: "), sg.InputText(key='-input-')],
    [sg.Button("Dodaj"), sg.Button("Wypisz"), sg.Button("Wyjdz")],
    [sg.Text(" ", key='-output-')]
]

window = sg.Window("Wartosci liczbowe", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Wyjdz":
        break

    if event == "Dodaj":
        myList.append(values['-input-'])
        window['-input-'].update("")

    if event == "Wypisz":
        wynik = []
        for i in myList:
            try:
                value = int(i)
            except ValueError:
                continue
            wynik.append(value)
        window['-output-'].update(str(wynik))

window.close()
