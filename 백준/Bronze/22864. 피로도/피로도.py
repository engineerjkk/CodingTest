import sys
input = sys.stdin.readline
a,b,c,m=map(int,input().split())
i=0
ans=0
pi=0
work=0
while i<24:
    i+=1
    if pi+a<=m:
        pi+=a
        work+=b
    else:
        pi-=c
        pi=max(0,pi)
print(work)
    

