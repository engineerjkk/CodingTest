import sys 
input = sys.stdin.readline 
n=int(input())
tables=[-1]*200001

count=0
for _ in range(n):
    a,b=map(int,input().split())
    if b==1:
        if tables[a]==1:
            count+=1
        tables[a]=1
    else:
        if tables[a]==0 or tables[a]==-1:
            count+=1
        tables[a]=0
for i in range(200001):
    if tables[i]==1:
        count+=1
print(count)
