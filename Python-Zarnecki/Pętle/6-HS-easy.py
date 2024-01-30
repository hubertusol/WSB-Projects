
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Podaj liczbę całkowitą większą od 1: "))
print("Liczby pierwsze od 1 do", n, "to:")
for i in range(2, n + 1):
    if is_prime(i):
        print(i)
