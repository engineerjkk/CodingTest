import sys
input = sys.stdin.readline
s=str(input())
i=0
pol=["AAAA","BB"]
answer=""
while i<len(s)-1:
    if i+4<=len(s)and s[i:i+4]=="XXXX":
        answer+=pol[0]
        i+=4
    elif i+2<=len(s) and s[i:i+2]=="XX":
        answer+=pol[1]
        i+=2
    elif s[i]==".":
        answer+="."
        i+=1
    else:
        print(-1)
        exit()
print(answer)