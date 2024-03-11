text=input("Prosze wpisac liczbe n i liczbe k oddzielona spacjami: ")
n = int(text.split()[0])
k = int(text.split()[1])
if n>10000 or k>1000: exit()
while n>0:
    if n>=k:
        print(k,end=" ")
        n-=k
    else:
        print(n,end="")
        n=0