n = int(input("Prosze wpisac ilosc katow w wielokacie: "))
if n<0 or n>40: exit()
i=(n-2)*180/n
e=360/n
if i%1!=0 or e%1!=0:
    print("Miary katow nie sa liczbami naturalnymi")
    exit()
print(int(i),int(e),sep=" ")
if i%2==0 and e%2==0: print("even")
else: print("odd")