n=int(input())
for _ in range(n):
    s=input()
    if len(s)==2:
        print(s,end='')
    else:
        i=0
        while i<len(s):
            if i==0:
                print(s[0],end='')
            elif i==len(s)-1:
                print(s[-1],end='')
            else:
                if s[i]==s[i+1]:
                    print(s[i],end='')
                    i+=1
            i+=1
    print()