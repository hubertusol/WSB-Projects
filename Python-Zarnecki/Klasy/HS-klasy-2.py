class Kwadrat:
    def __init__(self, bok):
        self.bok =bok
    def obwod(self):
        return self.bok*4
    def pole(self):
        return self.bok**2
obiekt = Kwadrat(10)
print(obiekt.obwod(),obiekt.pole(),sep="\n")