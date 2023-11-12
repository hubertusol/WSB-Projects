import PySimpleGUI as sg
layout = [
    [sg.Text("Menu Główne")],
    [sg.Button("Dodaj zadanie")],
    [sg.Button("Wyświetl zadania")],
    [sg.Button("Usuń zadanie")],
    [sg.Button("Zakończ program")]
]
layout_dodaj = [
    [sg.Text("Dodawanie zadań")],
    [sg.InputText(key='-add-'),sg.Button("Dodaj")]
]
layout_wyswietl = [
    [sg.Text("Lista zadań")],
    [sg.Text(" ")]
]
zadania = ["Przykladowe1","Przykladowe2"]
window_menu = sg.Window("Menu głowne",layout)
window_add = sg.Window("Dodaj zadanie",layout_dodaj)


while True:
    event , values = window_menu.read()
    if event == "Zakończ program" or event == sg.WINDOW_CLOSED:
        break
    if event == "Dodaj zadanie":
        while True:
            event , values = window_add.read()
            if event == sg.WINDOW_CLOSED:
                window_add.close()
                break
            if event == "Dodaj":
                zadania.append(values['-add-'])
    if event == "Wyświetl zadania":
        for i,value in enumerate(zadania,1):
            layout_wyswietl.append([sg.Text(value)])
        window_list = sg.Window("Wyświetl zadania",layout_wyswietl)
        while True:
            event, values == window_list.read()
            if event == sg.WINDOW_CLOSED:
                window_list.close()
                break

