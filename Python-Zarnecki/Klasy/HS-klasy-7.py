import time
class Zegar:
    def __init__(self, minuta, sekunda):
        self.minuta = minuta
        self.sekunda = sekunda
    def ustaw_czas(self,s,h):
        self.godzina = h
        self.sekunda = s
    def odliczaj(self):
        while self.godzina>0 or self.sekunda>0:
            time.sleep(1)
            if self.sekunda>0:
                self.sekunda-=1
            else:
                self.sekunda=59
                self.godzina-=1
            print(f"{self.godzina}:{self.sekunda}")
czas = Zegar(0,0)
Zegar.ustaw_czas(czas, 10,10)
Zegar.odliczaj(czas)