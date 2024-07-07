#import sys
#input = sys.stdin.readline
T=int(input())
check={"A","B","C","D","E","F"}
for _ in range(T):
    s=input()
    if len(s)<3:
        print("Good")
        continue
    if s[0]!="A":
        if s[0] not in check:
            print("Good")
            continue
        s=s[1:]
    if s[-1] !="C":
        if s[-1] not in check:
            print("Good")
            continue
        s=s[:-1]
    ans=""
    for i in range(len(s)):
        if i==0 or s[i]!=s[i-1]:
            ans+=s[i]
    if ans=="AFC":
        print("Infected!")
    else:
        print("Good")
        
        