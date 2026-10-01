word=input()
l=0
u=0
for ch in word:
    if ch.islower():
        l+=1
    else:
        u+=1
if l>=u:
    print(word.lower())
else:
    print(word.upper())