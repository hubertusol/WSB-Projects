import math
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r*self.r*math.pi
    def circumference(self):
        return 2*self.r*math.pi
while True:
    try: radius = int(input("Prosze wpisac dlugosc promienia: "))
    except ValueError: break
    okrag=Circle(radius)
    print(f"Pole okregu: {okrag.area()}")
    print(f"Obwod okregu: {okrag.circumference()}")
    print("Aby zakonczyc program, wpisz cokolwiek poza liczbą")
