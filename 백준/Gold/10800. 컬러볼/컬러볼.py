import sys 
input = sys.stdin.readline 
n=int(input())
balls=[[] for _ in range(2001)]
for id in range(n):
    c,s=map(int,input().split())
    balls[s].append((c,id))

count={}
answer=[0]*n 
total=0
for i in range(1,2001):
    for c,id in balls[i]:
        if c not in count:
            count[c]=0 
        answer[id]=total-count[c]
    total+=i*len(balls[i])
    for c,id in balls[i]:
        count[c]+=i 
for i in range(n):
    print(answer[i])
