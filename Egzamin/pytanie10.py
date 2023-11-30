def fibonacci(n):
    if n <= 0:
        return "Proszę podać liczbę naturalną większą od zera."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
n = int(input("Podaj liczbę naturalną n: "))
wynik = fibonacci(n)
print(f"{n}-ty wyraz ciągu Fibonacciego: {wynik}")