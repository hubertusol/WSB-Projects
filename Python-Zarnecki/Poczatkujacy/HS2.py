#Liczenie BMI
try:
    waga = int(input("Wpisz wagę w kilogramach: "))
    wzrost = int(input("Wpisz wzrost w centymetrach: "))
except:
    print("Błąd zmiennej")
wzrost /= 100
BMI = waga/wzrost**2
print("Bmi jest równe " ,BMI)
