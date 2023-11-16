tasks = [
'''
for i in range(1, 11):
    print(i)
''',
'''
num = 10
while num >= 1:
    print(num)
    num -= 1
''',
'''
for i in range(2, 51, 2):
    print(i)
''',
'''
n = int(input("Podaj liczbę całkowitą dodatnią: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Suma liczb od 1 do", n, "to:", sum)
''',
'''
n = int(input("Podaj liczbę całkowitą: "))
print(f"Tabliczka mnożenia dla {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
''',
'''
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
''',
'''
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)
    return sequence[:n]

n = int(input("Podaj liczbę całkowitą większą od 0: "))
print(f"Pierwsze {n} liczb Fibonacciego:")
print(fibonacci(n))
''',
'''
numbers = [int(x) for x in input("Podaj listę liczb oddzielonych spacjami: ").split()]
max_value = max(numbers)
min_value = min(numbers)
print("Największa wartość:", max_value)
print("Najmniejsza wartość:", min_value)
''',
'''
numbers = [int(x) for x in input("Podaj listę liczb oddzielonych spacjami: ").split()]
search_num = int(input("Podaj liczbę do sprawdzenia: "))
if search_num in numbers:
    print(f"Liczba {search_num} znajduje się na liście.")
else:
    print(f"Liczba {search_num} nie znajduje się na liście.")
''',
'''
string = input("Podaj ciąg znaków: ")
character_count = {}
for char in string:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1

print("Wystąpienia każdego znaku:")
for char, count in character_count.items():
    print(f"'{char}': {count}")
''',
'''
string = input("Podaj ciąg znaków: ")
reversed_string = string[::-1]
print("Odwrócony ciąg znaków:", reversed_string)
''',
'''
string = input("Podaj ciąg znaków: ")
if string == string[::-1]:
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")
''',
'''
decimal_number = int(input("Podaj liczbę dziesiętną: "))
binary_number = bin(decimal_number)
print("Liczba w systemie binarnym:", binary_number)
''',
'''
list1 = [int(x) for x in input("Podaj pierwszą listę liczb oddzielonych spacjami: ").split()]
list2 = [int(x) for x in input("Podaj drugą listę liczb oddzielonych spacjami: ").split()]
common_elements = list(set(list1) & set(list2))
print("Wspólne elementy obu list:")
print(common_elements)
''',
'''
numbers = [int(x) for x in input("Podaj listę liczb oddzielonych spacjami: ").split()]
average = sum(numbers) / len(numbers) if len(numbers) > 0 else 0
print("Średnia z podanych liczb:", average)
'''
]

for i, task_code in enumerate(tasks, start=1):
    filename = f"{i}-HS-easy.py"
    with open(filename, 'w') as file:
        file.write(task_code)
    print(f"Utworzono plik: {filename}")