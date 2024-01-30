
numbers = [int(x) for x in input("Podaj listę liczb oddzielonych spacjami: ").split()]
average = sum(numbers) / len(numbers) if len(numbers) > 0 else 0
print("Średnia z podanych liczb:", average)
