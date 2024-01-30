import PySimpleGUI as sg
layout = [
    [sg.Text(" ",key="-output-")],
    [sg.Button("Pokaz"),sg.Button("Wyjdz")]
]
window = sg.Window(" ", layout)
mylist = []
def countNumbers():
    for i in range(1,101):
        mylist.append(i)
    for x in mylist:
        if x % 7 !=0 or x %5 == 0:
            mylist.remove(x)
while True:
    event, values = window.read()
    countNumbers()
    if event == "Pokaz":
        window['-output-'].update(mylist)
    if event == sg.WINDOW_CLOSED or event == "Wyjdz":
        break
window.close()