t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    min_=min(a)
    print(n-min_)