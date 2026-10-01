n=int(input())
w1="I hate"
w2="I love"
for i in range(n):
    if i%2==0:
        print(w1,end=' ')
    else:
        print(w2,end=' ')
    if i==n-1:
        print("it")
    else:
        print("that",end=' ')