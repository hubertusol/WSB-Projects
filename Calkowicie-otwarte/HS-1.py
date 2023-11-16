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
    [sg.InputText(key='-add-',do_not_clear=False),sg.Button("Dodaj"),sg.Button("Cofnij",key='-back-')],
    [sg.Text(" ")]
]
layout_wyswietl = [
    [sg.Text("Lista zadań"),sg.Button("Cofnij",key='-back-')],
    [sg.Text("----------------",key='-output-')],
]
layout_usun = [
    [sg.Text("Usuwanie zadania"),sg.Button("Cofnij",key='-back-')],
    [sg.Text("Wpisz numer zadania które ma byc usuniete: "),sg.InputText(" ",key='-remove-',do_not_clear=False),sg.Button("Usun")],
    [sg.Text(" ",key='-message-')]
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
zadania = ["Przykladowe1","Przykladowe2"]
window = sg.Window("Menu głowne",layout)
for i, task in enumerate(zadania,start=1):
    zadania[i-1]=str(i)+". "+task
    print(zadania)
while True:
    event , values = window.read()
    if event == "Zakończ program" or event == sg.WINDOW_CLOSED:
        break
    if event.startswith("-back-") :
        clear_layouts('-menu-')
    if event == "Dodaj zadanie":

        clear_layouts('-dodaj-')
    if event == "Wyświetl zadania":
        layout[0][2].update(visible=True)
        layout_wyswietl = layout_wyswietl[:2]
        for i, task in enumerate(zadania,start=1):
            try:
                task = task.split('. ')[1]
            except IndexError:
                print("haha")
            zadania[i-1]=str(i)+". "+task
            nowy_element = '\n'.join(zadania)
            window['-output-'].update(nowy_element)
            window.finalize()
            window.Refresh()
        print(len(layout_wyswietl))
        clear_layouts('-wyswietl-')
    if event == "Usuń zadanie":
        clear_layouts('-usun-')

    if event == "Dodaj":
        zadania.append(values['-add-'])
    if event == "Usun":
        try: 
            wybor = int(values['-remove-'])
            if wybor-1 in range(0,len(zadania)):
                zadania.pop(wybor-1)
                window["-message-"].update("Zadanie pomyslnie usuniete!")
            else:
                window["-message-"].update("Niepoprawny numer zadania")
        except ValueError:  window["-message-"].update("Prosze wpisac liczbe")
window.close()