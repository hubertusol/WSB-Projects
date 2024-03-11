n = int(input("Prosze wpisac liczbe n: "))
if n<0 or n>1000: exit()
#specjalny przypadek: n=1
if n==1:
    print("#")
    exit()
#pierwsza linijka
for i in range(0,n):
    print("#",end="")
print("")
#linijki wewnetrzne
for i in range(0,n-2):
    print("#",end="")
    #miejsca puste
    for x in range(0,n-2):
        print(" ",end="")
    print("#",end="")
    print("")
#linijka koncowa
for i in range(0,n):
    print("#",end="")