import sys 
input = sys.stdin.readline 

n,m=map(int,input().split())
c=[]
for _ in range(m):
    c.append(list(map(int,input().split())))

c.sort(reverse=True)
cost=0
for i in range(m-1):
    if c[i][0]<n:
        cost+=n-c[i][0]
print(cost)