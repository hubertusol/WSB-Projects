import random
import timeit
#Hubert Sołtys
#ciag A zostanie zapełniony losowymi liczbami od 0 do 100
#liczba wyrazów ciągu A zostanie wybrana przez uzytkownika
#program posortuje ciąg oraz zmierzy czas potrzebny na wykonanie skryptu
try: 
    dlugosc = int(input("Proszę wybrać długość ciągu do posortowania: "))
    if dlugosc<2: 
        print("Liczba musi byc wieksza od 1")
        exit()
except ValueError:
    print("Proszę wybrac liczbe naturalna")
    exit()
A = []
for i in range(0,dlugosc):
    A.append(random.randrange(100))
print("Oto otrzymany ciąg losowych liczb: ",A,sep="\n")
def zamiana(x,y): #zamiana wyrazów ciagu miejscami
    temp=A[x]
    A[x]=A[y]
    A[y]=temp
def sortujCiag(p,q):
    if p!=q:
        print(p,q)
        k=(q-p+1)//2
        for i in range(1,k+1):
            print("zamieniam: ",p+i-2,q-k+i-1)
            zamiana(p+i-2,q-k+i-1)
        sortujCiag(p-1,p+k-2)
        sortujCiag(q-k,q-1)
empty=input("Wcisnij ENTER gdy bedziesz gotowy!")
print("Czas start!")
start = timeit.default_timer()
sortujCiag(1,dlugosc)
stop = timeit.default_timer()
print("Stop! Sortowanie trwało: ",stop-start," sekund")
print("Oto posortowana lista: ",A,sep="\n")
