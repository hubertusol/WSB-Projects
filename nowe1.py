import PySimpleGUI as sg
def even_number(input):
    count = (input+1)//2
    return count
layout = [
    [sg.Text("Wpisz liczbę: "),sg.InputText(key='-input-')],
    [sg.Button("Oblicz"),sg.Button("Wyjdz")],
    [sg.Text("Liczba parzystych liczb"),sg.Text("0",key='-output-')]
]
window = sg.Window("Liczby parzyste", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Wyjdz":
        break
    if event == "Oblicz":
        try:
            x = int(values['-input-'])
            even = even_number(x)
            window['-output-'].update(str(even))
        except ValueError:
            sg.popup_error('Podana wartość nie jest liczbą całkowitą')
window.close()
