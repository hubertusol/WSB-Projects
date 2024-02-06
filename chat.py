import random
import timeit

# Hubert Sołtys
# Ciąg A zostanie zapełniony losowymi liczbami od 0 do 100
# Liczba wyrazów ciągu A zostanie wybrana przez użytkownika
# Program posortuje ciąg oraz zmierzy czas potrzebny na wykonanie skryptu

try:
    dlugosc = int(input("Proszę wybrać długość ciągu do posortowania: "))
    if dlugosc < 2:
        print("Liczba musi być większa od 1")
        exit()
except ValueError:
    print("Proszę wybrać liczbę naturalną")
    exit()

A = [random.randrange(100) for _ in range(dlugosc)]
print("Oto otrzymany ciąg losowych liczb: ", A, sep="\n")

def zamiana(x, y):
    # Zamiana wyrazów ciągu miejscami
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def sortujCiag(p, q):
    if p < q:
        k = (q - p + 1) // 2
        for i in range(k):
            zamiana(p + i, q - k + i)
        sortujCiag(p, p + k - 1)
        sortujCiag(q - k + 1, q)

empty = input("Wciśnij ENTER gdy będziesz gotowy!")
print("Czas start!")
start = timeit.default_timer()
sortujCiag(0, dlugosc - 1)  # Poprawione indeksowanie, zaczynamy od 0
stop = timeit.default_timer()
print("Stop! Sortowanie trwało: ", stop - start, " sekund")
print("Oto posortowana lista: ", A, sep="\n")
