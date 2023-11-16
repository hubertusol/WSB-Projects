
numbers = [int(x) for x in input("Podaj listę liczb oddzielonych spacjami: ").split()]
unique_numbers = list(set(numbers))
print("Lista bez duplikatów:", unique_numbers)
