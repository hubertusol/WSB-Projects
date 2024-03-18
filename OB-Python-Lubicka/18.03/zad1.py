numbers = ['1','2','3','4','5','6','7','8','9']
s = input()
list = []
for i in range(9):
    if numbers[i] not in s:
        print(numbers[i])