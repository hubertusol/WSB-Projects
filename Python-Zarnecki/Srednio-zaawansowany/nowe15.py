import PySimpleGUI as sg
mylist = []
layout = [
    [sg.Text("Proszę wpisać liczbę: "),sg.InputText(key='-input-')],
    [sg.Button("Dodaj"),sg.Button("Oblicz"),sg.Button("Wyjdz")],
    [sg.Text(" ",key='-output-')]
]
def obliczNajwyzszy(input):
    temp_number = -999999999999
    for i in input:
        if i > temp_number:
            temp_number=i
    return temp_number


window = sg.Window("Najwieksza liczba" ,layout)

while True:
    event, values = window.read()
    if  event == "Wyjdz" or event == sg.WINDOW_CLOSED:
        break
    if event == "Dodaj":
        try: 
            liczba = int(values['-input-'])
            mylist.append(liczba)
        except ValueError:
            continue
    if event == "Oblicz":
        window['-output-'].update(obliczNajwyzszy(mylist))
window.close()