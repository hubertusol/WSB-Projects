tasks=[{'description':'Przykładowe zadanie','completed':False}]

def main():
    while True:
        print("--- Lista zadań ---\n")
        print_tasks()
        print("--- Wybierz opcję ---")
        print("1. Dodawanie zadania")
        print("2. Oznacz zadanie jako wykonane")
        print("3. Usuń zadanie")
        print("4. Wyjdź")
        try: wybor=int(input("Twój wybór: "))
        except ValueError: print("Niepoprawna zmienna")
        if wybor == 1: add_task()
        elif wybor == 2: complete_task()
        elif wybor == 3: remove_task()
        elif wybor == 4: break

def print_tasks():
    for i, task in enumerate(tasks, 1):
        if task['completed']== True: status="[x]"
        else: status= "[ ]"
        print(status,str(i)+'.',task['description'],sep=" ")
def add_task():
    opis=input("Proszę wpisać opis zadania: ")
    tasks.append({'description':opis,'completed':False})
def complete_task():
    while True:
        try: x=int(input("Proszę wybrać numer zadania do oznaczenia jako wykonany: "))
        except ValueError: print("Niepoprawna zmienna")
        if x>0 and x<=len(tasks):
            tasks[x-1]['completed']=True
            print(tasks[x-1])
            break
def remove_task():
    while True:
        try: y=int(input("Proszę wybrać numer zadania do usuniecia: "))
        except ValueError: print("Niepoprawna zmienna")
        if y>0 and y<=len(tasks):
            tasks.pop(y-1)
            break
main()