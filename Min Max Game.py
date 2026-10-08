t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    one=a.count(1)
    zero=a.count(0)
    if one>=zero:
        print("Bessie")
    else:
        print("Elsie")