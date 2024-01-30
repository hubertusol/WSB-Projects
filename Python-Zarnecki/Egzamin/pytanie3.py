vowels = {'a','e','i','o','u'}
wspolgloski = {'b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','u','v','w','x','y','z','ż','ź','ó','ś','ą','ę','ć','ń'}
tekst = input("Wpisz dowolny tekst: ")
liczba_samoglosek = 0
liczba_wspolglosek = 0
liczba_num = 0
tekst.lower()
for i in tekst:
    if i in vowels: liczba_samoglosek+=1
    elif i in wspolgloski: liczba_wspolglosek+=1
    else: liczba_num+=1
print(f"Liczba samoglosek: {liczba_samoglosek}")
print(f"Liczba wspolglosek: {liczba_wspolglosek}")
print(f"Liczba numerow lub znakow specjalnych: {liczba_num}")