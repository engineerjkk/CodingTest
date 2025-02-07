import sys 
input = sys.stdin.readline 
from collections import deque 

a,b,c=map(int,input().split())
s=a+b+c 
if s%3!=0:
    print(0)
else:
    queue=deque()
    queue.append((a,b))
    visit=[[False]*s for _ in range(s)]
    visit[a][b]=True 
    while queue:
        a,b=queue.popleft()
        c=s-a-b 
        d=[a,b,c]
        for i in range(3):
            x,y=d[i],d[(i+1)%3]
            if x==y:
                continue 
            if x>y:
                x,y=y,x 
            if not visit[x+x][y-x]:
                visit[x+x][y-x]=True 
                queue.append((x+x,y-x))
    if visit[s//3][s//3]:
        print(1)
    else:
        print(0)
        
