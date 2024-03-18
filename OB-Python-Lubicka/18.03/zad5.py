n,k = [int(i) for i in input().split()]

carrots = []
while n>0:
    carrot = min(n,k)
    carrots.append(carrot)
    n-=k
print(*carrots)