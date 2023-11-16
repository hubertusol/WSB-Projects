import math
class Punkt:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def odleglosc(self):
        wartosc = math.sqrt((self.x**2+self.y**2))
        return wartosc
punkt1 = Punkt(3,4)
punkt2 = Punkt(-5,-12)
print(punkt1.odleglosc())
print(punkt2.odleglosc())