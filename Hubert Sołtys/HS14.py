guests = ['Marian','Mariusz','Maciej']
potrawy = ['Sałatka','Karkówka','Szynka']
harmonogram = ['Grill', 'Picie']
def listElements(elements):
    for i, element in enumerate(elements,1):
        print(i,element,sep=". ")
def addElement(elements):
    dodaj=input("Wpisz, co chcesz dodać do listy: ")
    elements.append(dodaj)
def removeElement(elements):
    try: usun=int(input("Wybierz numer elementu, który chcesz usunąć: "))
    except ValueError: print("Błędny numer!")
    if usun>0 and usun<=len(elements):
        print(elements)
        elements.pop(usun-1)
while True:
    print("--- Menu głowne ---")
    print("1. Goście")
    print("2. Potrawy")
    print("3. Harmonogram")
    print("4. Wyjdź")
    try: wybor=int(input("Twoj wybor: "))
    except ValueError: print("Błędny numer!")
    if wybor==1:
        print("--- Goście ---")
        temp=guests
        listElements(guests)
    elif wybor==2:
        print("--- Potrawy ---")
        listElements(potrawy)
        temp=potrawy
    elif wybor==3:
        print("--- Harmonogram ---")
        listElements(harmonogram)
        temp=harmonogram
    elif wybor==4: break
    else:
        print("Wybierz prawidłowy numer")
    print("--- Opcje ---")
    print("1. Dodawanie elementu")
    print("2. Usuwanie elementu")
    print("3. Wyjście z programu")
    try: opcja=int(input("Proszę wybrać działanie: "))
    except ValueError: print("Błędny numer!")
    if opcja==1: addElement(temp)
    elif opcja==2: removeElement(temp)
    elif opcja==3: break
    else:
        print("Wybierz prawidłowy numer")
    