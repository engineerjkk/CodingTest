import sys
input = sys.stdin.readline

n,t=map(int,input().split())
a=[]
for i in range(1,2*n+1):
    a.append(i)
for i in reversed(range(2,2*n)):
    a.append(i)

t-=1
t=t%(4*n-2)

print(a[t])
