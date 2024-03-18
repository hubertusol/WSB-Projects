class Cat:
    def __init__(self,masa,dlugosc_zycia,predkosc):
        self.masa=masa
        self.dlugosc_zycia=dlugosc_zycia
        self.predkosc=predkosc
    def __str__(self):
        return f"Kot waży {self.masa}kg, średnio żyje {self.dlugosc_zycia} lat, może biec z maksymalną prędkością {self.predkosc} km/h"
    class Tiger:
        def __init__(self,masa,dlugosc_zycia,predkosc, umaszczenie):
            Cat.__init__(self,masa,dlugosc_zycia,predkosc)
            self.umaszczenie=umaszczenie
        def __str__(self):
            return f"Tygrys waży {self.masa}kg, średnio żyje {self.dlugosc_zycia} lat, może biec z maksymalną prędkością {self.predkosc} km/h oraz ma {self.umaszczenie} umaszczenie"
dachowiec=Cat(5,14,20)
print(dachowiec)
tygrys=Cat.Tiger(310,26,65,"pręgowate")
print(tygrys)