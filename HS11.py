try:
    dochod =float(input("Wpisz swój dochód roczny: "))
    kup = float(input("Wpisz swój koszt uzyskania przychodu: "))
except ValueError:
    print("Błąd zmiennej")
if dochod>0:
    kwota = dochod-kup
    emerytalna = 0.0975*kwota 
    rentowa = 0.015*kwota 
    chorobowa = 0.045*kwota 
    zdrowotna = 0.09*kwota 
    podstawa_opodatkowania = (kwota -(emerytalna+rentowa+chorobowa+zdrowotna))-30000 #odliczam składki i kwotę wolną od podatku

    if podstawa_opodatkowania<=120000:
        podatek_dochodowy=0.12*podstawa_opodatkowania
    else:
        podatek_dochodowy=14400+0.32*(podstawa_opodatkowania-120000)
    if podstawa_opodatkowania<=0: 
        podatek_dochodowy=0
        podstawa_opodatkowania +=30000
    print("składka emerytalna: ",emerytalna)
    print("składka chorobowa: ",chorobowa)
    print("składka rentowa: ",rentowa)
    print("składka zdrowotna: ",zdrowotna)
    print("Podstawa opodatkowania: ",podstawa_opodatkowania)
    print("Kwota podatku dochodowego: ", podatek_dochodowy)
    print("Zostałeś orżnięty na: ",emerytalna+rentowa+chorobowa+zdrowotna+podatek_dochodowy)
    print("Po wszystkim zostało ci: ",podstawa_opodatkowania-podatek_dochodowy)
else:
    print("Dochód nie może być mniejszy niż 0")