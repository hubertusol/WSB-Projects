n,k = [int(i) for i in input().split()]

rest = n%k

if rest ==0:
    for i in range(n,n+1,k):
        print(k,end="")
        print(" ", end="")
else:
    for i in range(k,n+1,k):
        print(k,end="")
        print(" ",end="")
    print(rest,end="")