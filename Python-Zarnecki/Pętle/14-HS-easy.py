
list1 = [int(x) for x in input("Podaj pierwszą listę liczb oddzielonych spacjami: ").split()]
list2 = [int(x) for x in input("Podaj drugą listę liczb oddzielonych spacjami: ").split()]
common_elements = list(set(list1) & set(list2))
print("Wspólne elementy obu list:")
print(common_elements)
