T=int(input())
check={"A","B","C","D","E","F"}
for _ in range(T):
    s=str(input())
    if len(s)<3:
        print("Good")
        continue
    if s[0]!="A":
        if s[0] not in check:
            print("Good")
            continue
        s=s[1:]
    if s[-1]!="C":
        if s[-1] not in check:
            print("Good")
            continue
        s=s[:-1]
    ans=s[0]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            ans+=s[i]
    if ans=="AFC":
        print("Infected!")
    else:
        print("Good")