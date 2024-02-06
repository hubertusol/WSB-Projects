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
        k=(q-p+1)//2
        for i in range(1,k+1):
            zamiana(A[p+i-1],A[q-k+i])
        sortujCiag(p,p+k-1)
        sortujCiag(q-k+1,q)
empty=input("Wcisnij ENTER gdy bedziesz")
start = timeit.timeit()
sortujCiag(1,dlugosc)
stop = timeit.timeit()
print("Stop! Sortowanie trwało: ",stop-start," sekund")
print("Oto posortowana lista: ",A,sep="\n")
