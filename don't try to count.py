n=int(input())
def fun(s1,s2):
    c=0
    while s2 not in s1:
        s1+=s1
        c+=1
        if len(s2)*3<len(s1) and s2 not in s1:
            return -1
    return c

for i in range(n):
    n,m=map(int,input().split())
    s1=input().strip()
    s2=input().strip()
    print(fun(s1,s2))