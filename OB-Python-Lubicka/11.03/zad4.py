n = int(input("Prosze wpisac liczbe naturalna n: "))
wynik=[]
for a in range(1,n+1):
    if a%3==0 and a%5==0:
        wynik.append("FizzBuzz")
    elif a%3==0:
        wynik.append("Fizz")
    elif a%5==0:
        wynik.append("Buzz")
    else: wynik.append(a)
print(wynik)