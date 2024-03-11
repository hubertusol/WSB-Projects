file = open("d:/WSB-Projects/OB-Python-Lubicka/Names.txt","r")
lista = []
for line in file:
    lista.append(line.rstrip())
print(lista)
file.close()
wybor = input("Prosze wpisac jedno z imion: ")
if wybor in lista:
    lista.remove(wybor)
    file_new = open("d:/WSB-Projects/OB-Python-Lubicka/Names2.txt","x")
    file_new.close()
    file_new = open("d:/WSB-Projects/OB-Python-Lubicka/Names2.txt","a")
    for name in lista:
        file_new.write(f"{name}\n")

