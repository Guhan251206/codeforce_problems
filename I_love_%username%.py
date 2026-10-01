n=int(input())
arr=list(map(int,input().split()))
maxi=arr[0]
mini=arr[0]
count=0
for i in range(1,n):
    if arr[i]>maxi or arr[i]<mini:
            count+=1
    maxi=max(arr[i],maxi)
    mini=min(arr[i],mini)
print(count)