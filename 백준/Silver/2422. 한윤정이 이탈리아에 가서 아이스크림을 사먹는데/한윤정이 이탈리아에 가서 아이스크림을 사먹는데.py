import sys 
input = sys.stdin.readline 
from itertools import combinations 

n,m = map(int,input().split())
icecream=set()
for _ in range(m):
    a,b=map(int,input().split())
    icecream.add((a,b))
    icecream.add((b,a))
cream=list(range(1,n+1))
cnt=0
for com in combinations(cream,3):
    d=[com[0],com[1],com[2]]
    flag=True
    for i in range(3):
        a=d[i]
        b=d[(i+1)%3]
        if (a,b) in icecream:
            break
    else:
        cnt+=1
print(cnt)
