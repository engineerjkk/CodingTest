import sys
input = sys.stdin.readline

n=int(input())

answer=[]
for _ in range(n):
    a,b=map(int,input().split())
    time=b-a
    if time>=0:
        answer.append(b)
if len(answer)>0:
    print(min(answer))
else:
    print(-1)
