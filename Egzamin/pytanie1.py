import random
losowe_liczby = []
for i in range(0,10):
    losowe_liczby.append(random.randint(1,50))
najwieksza = max(losowe_liczby)
najmniejsza = min(losowe_liczby)
print(f"Najwieksza: {najwieksza}")
print(f"Najmniejsza: {najmniejsza}")