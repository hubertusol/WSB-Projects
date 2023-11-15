import PySimpleGUI as sg

# Inicjalizacja listy zadań
tasks = []

# Funkcja dodająca zadanie do listy
def add_task(task):
    tasks.append(task)

# Funkcja zaznaczająca zadanie jako zakończone
def complete_task(index):
    if index < len(tasks):
        tasks[index] = "[x] " + tasks[index]

# Funkcja usuwająca zadanie z listy
def delete_task(index):
    if index < len(tasks):
        del tasks[index]

# Funkcja wyświetlająca listę zadań
def display_tasks():
    if not tasks:
        sg.popup("Lista zadań jest pusta!")
    else:
        task_list = [f"{i+1}. {task}" for i, task in enumerate(tasks)]
        sg.popup('\n'.join(task_list))

# Interfejs graficzny
layout = [
    [sg.Text('Zarządzanie listą zadań')],
    [sg.Button('Dodaj zadanie'), sg.Button('Wyświetl zadania'), sg.Button('Usuń zadanie'), sg.Button('Zakończ program')]
]

window = sg.Window('Lista zadań', layout)

while True:
    event, _ = window.read()

    if event == sg.WIN_CLOSED or event == 'Zakończ program':
        break
    elif event == 'Dodaj zadanie':
        task = sg.popup_get_text('Wpisz treść zadania:')
        if task:
            add_task(task)
    elif event == 'Wyświetl zadania':
        display_tasks()
    elif event == 'Usuń zadanie':
        index = sg.popup_get_text('Podaj numer zadania do usunięcia:')
        if index.isdigit():
            index = int(index) - 1
            if 0 <= index < len(tasks):
                delete_task(index)
                sg.popup('Zadanie zostało usunięte.')
            else:
                sg.popup('Podano niepoprawny numer zadania!')
        else:
            sg.popup('Podaj numer zadania jako liczbę!')

window.close()
