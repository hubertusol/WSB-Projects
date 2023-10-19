slowo = "kazakstan"
ukryte_slowo = '_' * len(slowo)
proby=10
def znajdz_litere(litera,slowo,ukryte):
    indeksy = []
    lista = list(ukryte)
   # lisslo = list(slowo)
   # print(lista)
    for i, litera_slowo in enumerate(slowo):
        if litera.lower() == litera_slowo:
            indeksy.append(i)
            #print(indeksy)
            for x in indeksy:
                lista[i]=litera_slowo
              #  print("".join(lista))
    return "".join(lista)
for proby in range(proby,0,-1):
    print("Pozostalo prob: ", proby)
    print("Ukryte słowo: \n",ukryte_slowo)
    litera=input("Wpisz litere: ")
    
    if len(litera)==1 and litera in slowo:
        print("Brawo! litera znadjuje sie w tekscie")
        ukryte_slowo=znajdz_litere(litera,slowo,ukryte_slowo)
    if '_' not in ukryte_slowo:
        print("Gratulacje, wygrales!")
        break


