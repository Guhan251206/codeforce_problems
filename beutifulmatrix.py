a=[]
for i in range(5):
    a.append(list(map(int,input().split())))
r2,c2=0,0
r1,c1=2,2
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            r2=i
            c2=j
            
print(abs(r1-r2)+abs(c1-c2))