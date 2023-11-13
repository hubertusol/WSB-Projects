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
    [sg.InputText(key='-add-'),sg.Button("Dodaj"),sg.Button("Cofnij",key='-back-')],
    [sg.Text(" ")]
]
layout_wyswietl = [
    [sg.Text("Lista zadań"),sg.Button("Cofnij",key='-back-')],
    [sg.Text("----------------")],
    [sg.Listbox(values='1')]
]
layout_usun = [
    [sg.Text("Usuwanie zadania"),sg.Button("Cofnij",key='-back-')],
    [sg.Text(" ")]
]
layout = [
    [sg.Column(layout_menu,key='-menu-'),
    sg.Column(layout_dodaj,visible=False,key='-dodaj-'),
    sg.Column(layout_wyswietl,visible=False,key='-wyswietl-'),
    sg.Column(layout_usun,visible=False,key='-usun-')]
]
def clear_layouts(remaining_layout_key):
    for column in layout[0]:
        
        if column.key != remaining_layout_key:
            column.update(visible=False)
        else: 
            column.update(visible=True)
        #print(column.key,column.visible)
    
    window.refresh()
def update_layout(input_layout):
    layout[0][2].update(visible=True)  # Make sure the layout is visible
    input_layout[2:] = []  # Clear existing tasks
    for i, task in enumerate(zadania, start=1):
        input_layout.append([sg.Text(f"{i}. {task}")])
    window.refresh()
zadania = ["Przykladowe1","Przykladowe2"]
window = sg.Window("Menu głowne",layout)

while True:
    event , values = window.read()
    if event == "Zakończ program" or event == sg.WINDOW_CLOSED:
        break
    if event.startswith("-back-") :
        clear_layouts('-menu-')
    if event == "Dodaj zadanie":
        clear_layouts('-dodaj-')
    if event == "Wyświetl zadania":
        update_layout(layout_wyswietl)
        clear_layouts('-wyswietl-')
    if event == "Usuń zadanie":
        clear_layouts('-usun-')