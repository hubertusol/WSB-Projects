
def fibonacci_number(index):
    sequence = [0, 1]
    if index <= 1:
        return sequence[index]
    else:
        for i in range(2, index + 1):
            next_num = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_num)
        return sequence[index]
    