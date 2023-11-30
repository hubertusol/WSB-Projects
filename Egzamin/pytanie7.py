import math
try: 
    r=int(input("Prosze wpisac dlugosc promienia w cm: "))
    pole=round(math.pi*r**2,2)
    obwod=round(math.pi*r*2,2)
    print(f"Pole koła = {pole}")
    print(f"Obwód koła = {obwod}")
except ValueError: print("Prosze wpisac poprawna dlugosc")