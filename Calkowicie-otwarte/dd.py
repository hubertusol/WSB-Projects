import PySimpleGUI as sg

layout_menu = [
    [sg.Text("Menu Główne")],
    [sg.Button("Dodaj zadanie")],
    [sg.Button("Wyświetl zadania")],
    [sg.Button("Usuń zadanie")],
    [sg.Button("Zakończ program")]
]

layout_dodaj = [
    [sg.Text("Dodawanie zadań")],
    [sg.InputText(key='-add-'), sg.Button("Dodaj"), sg.Button("Cofnij")],
    [sg.Text(" ")]
]

layout_wyswietl = [
    [sg.Text("Lista zadań"), sg.Button("Cofnij")],
    [sg.Text("----------------")]
]

layout_usun = [
    [sg.Text("Usuwanie zadania"), sg.Button("Cofnij")],
    [sg.Text(" ")]
]

layout = [
    layout_menu,
    layout_dodaj,
    layout_wyswietl,
    layout_usun
]

def clear_layouts(remaining_layout_key):
    for i, column in enumerate(layout):
        if i == 2:  # Assuming the 'layout_wyswietl' is at index 2
            # Handling visibility differently for 'layout_wyswietl' list
            for element in column:
                element[0].update(visible=(element == layout[2][1][0]))
        elif column[0].key != remaining_layout_key:
            # Assuming the first element in each list represents the 'sg.Text' element
            column[0].update(visible=False)
        else:
            column[0].update(visible=True)

def update_layout(input_layout, tasks):
    input_layout[1][0].update(visible=True)  # Make sure the layout is visible
    input_layout[1][1:] = []  # Clear existing tasks
    for i, task in enumerate(tasks, start=1):
        input_layout.append([sg.Text(f"{i}. {task}")])

zadania = ["Przykladowe1", "Przykladowe2"]
window = sg.Window("Menu głowne", layout)

while True:
    event, values = window.read()
    if event == "Zakończ program" or event == sg.WINDOW_CLOSED:
        break
    if event == "Cofnij":
        clear_layouts('-menu-')
    if event == "Dodaj zadanie":
        clear_layouts('-dodaj-')
    if event == "Wyświetl zadania":
        update_layout(layout_wyswietl, zadania)
        clear_layouts('-wyswietl-')
    if event == "Usuń zadanie":
        clear_layouts('-usun-')

window.close()
