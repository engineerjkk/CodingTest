import sys
input = sys.stdin.readline
n=int(input())
m=int(input())
s=str(input())

current,cnt,answer=0,0,0
while current<m-1:
    if s[current:current+3]=="IOI":
        current+=2
        cnt+=1
        if cnt==n:
            cnt-=1
            answer+=1
    else:
        cnt=0
        current+=1
print(answer)