#Palindrom
slowo = input("Wpisz slowo: ")
slowo=slowo.lower().replace(' ', '')
odwrocone_slowo = ""
for i in range(len(slowo),0,-1):
     odwrocone_slowo +=slowo[i-1]
if odwrocone_slowo==slowo:
    print("Słowo jest palindromem")
else:
    print("Slowo nie jest palindromem")