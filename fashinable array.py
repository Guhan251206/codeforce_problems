import math

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    total=0
    for val in arr:
        a=val
        while math.gcd(a,x)!=1:
            s=math.gcd(a,x)
            total+=s
            a-=s
            if a==0:
                break
    print(total)