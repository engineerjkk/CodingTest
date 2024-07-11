n=int(input())
s=str(input())

tmp=s[0]
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        tmp+=s[i]

red=0
blue=0
for i in tmp:
    if i=="R":
        red+=1
    elif i=="B":
        blue+=1

if red<blue:
    print(red+1)
else:
    print(blue+1)