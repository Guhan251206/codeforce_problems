n=int(input())
t='codeforces'
for _ in range(n):
    s=input()
    c=0
    for i,ch in enumerate(s):
        if ch!=t[i]:
            c+=1
    print(c)