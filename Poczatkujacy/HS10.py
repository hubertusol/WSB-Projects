import random
import string
try: dlugosc = int(input("Wpisz długość hasła: "))
except ValueError: print("Błąd zmiennej")
password = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, dlugosc))
print("Twoje hasło: ",password,sep="\n")