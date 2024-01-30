objects = [
    '''
def square_number(number):
    return number ** 2
    ''',
    '''
def concatenate_strings(str1, str2):
    return f"{str1} {str2}"
    ''',
    '''
def find_max_number(numbers):
    return max(numbers)
    ''',
    '''
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0
    ''',
    '''
def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
    ''',
    '''
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
    ''',
    '''
def fibonacci_number(index):
    sequence = [0, 1]
    if index <= 1:
        return sequence[index]
    else:
        for i in range(2, index + 1):
            next_num = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_num)
        return sequence[index]
    ''',
    '''
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
    ''',
    '''
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
    ''',
    '''
def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all(letter in string.lower() for letter in alphabet)
    '''
]




for i, task_code in enumerate(objects, start=1):
    filename = f"{i}-HS-easy-funkcje.py"
    with open(filename, 'w') as file:
        file.write(task_code)
    print(f"Utworzono plik: {filename}")