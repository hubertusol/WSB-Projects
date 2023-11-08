import PySimpleGUI as sg
layout = [
    [sg.Text("Wpisz zdanie: "),sg.InputText(key="-input-")],
    [sg.Button("Oblicz"),sg.Button("Wyjdz")],
    [sg.Text(key="-output-")]
]
window = sg.Window("Liczenie spacji w zdaniu",layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Wyjdz":
        break
    if event == "Oblicz":
        zdanie = values["-input-"]
        wynik = 0
        for i in range(0,len(zdanie)):
            if zdanie[i]==' ':
                wynik+=1
        window["-output-"].update(wynik)