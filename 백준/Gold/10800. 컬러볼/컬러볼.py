import sys
input = sys.stdin.readline

n=int(input())
balls=[[] for _ in range(2001)]

for i in range(n):
    c,s=map(int,input().split())
    balls[s].append((c,i))

answer=[0]*n
total=0
count={}
for i in range(1,2001):
    for c,id in balls[i]:
        if c not in count:
            count[c]=0
        answer[id]=total-count[c]
    total+=i*len(balls[i])
    for c,_ in balls[i]:
        count[c]+=i

for i in range(n):
    print(answer[i])