check=["A","B","C","D","E","F"]
T=int(input())
for _ in range(T):
    s=str(input())
    if s[0] != "A":
        if s[0] not in check:
            print("Good")
            continue
        s=s[1:]
    if s[-1] !="C":
        if s[-1] not in check:
            print("Good")
            continue
        s=s[:-1]
    
    tmp=s[0]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            tmp+=s[i]
    if tmp=="AFC":
        print("Infected!")
    else:
        print("Good")