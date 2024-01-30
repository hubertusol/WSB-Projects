class KontoBankowe:
    def __init__(self, saldo):
        self.saldo=saldo
    def wplac(self, kwota):
        self.saldo+=kwota
        return self.saldo
    def wyplac(self,kwota):
        self.saldo-=kwota
        return self.saldo
konto = KontoBankowe(5000)
print(f"Po wpłacie na koncie jest {konto.wplac(2000)}zł")
print(f"Po wypłacie na koncie zostało {konto.wyplac(1500)}zł")