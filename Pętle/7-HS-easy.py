
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)
    return sequence[:n]

n = int(input("Podaj liczbę całkowitą większą od 0: "))
print(f"Pierwsze {n} liczb Fibonacciego:")
print(fibonacci(n))
