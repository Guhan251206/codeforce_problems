team=int(input())
arr=[list(map(int,input().split())) for _ in range(team)]
count=0
for i in range(team):
    for j in range(team):
        if i==j:
            continue
        if arr[i][0]==arr[j][1]:
            count+=1
print(count)