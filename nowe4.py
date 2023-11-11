import PySimpleGUI as sg
layout = [
    [sg.Text(" ",key="-output-")],
    [sg.Button("Wyjdz")]
]
window = sg.Window(" ", layout)
mylist = []
for i in range(0,101):
    mylist.append(i)
    print(mylist)
while True:
    event, values = window.read()
    window["-output-"].update(str(mylist))
    if event == sg.WINDOW_CLOSED or event == "Wyjdz":
        break