import sys
input = sys.stdin.readline

n,x=map(int,input().split())

lst=[]
answer=0
flag=False
for _ in range(n):
    waiting,time=map(int,input().split())
    if waiting+time<=x:
        answer=max(answer,waiting)
        flag=True
if flag:
    print(answer)
else:
    print(-1)