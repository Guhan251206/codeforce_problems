t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=n-k+1
    f=False
    total=0
    for i in range(s,n+1):
        if not f:
            total+=2**i
            f=True
        else:
            total+=2
    print(total)
            
