n=int(input())
c=0
for _ in range(n):
    a=list(map(int,input().split()))
    if a.count(1)>1:
        c+=1
print(c)