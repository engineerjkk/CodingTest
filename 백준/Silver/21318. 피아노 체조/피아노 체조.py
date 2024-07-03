import sys
input = sys.stdin.readline

n=int(input())
lst=[0]
lst+=list(map(int,input().split()))
q=int(input())
q_lst=[]
for _ in range(q):
    a,b=map(int,input().split())
    q_lst.append([a,b])

tmp=[0]*(n+1)
for i in range(n):
    if lst[i+1]-lst[i]<0:
        tmp[i]=1
    else:
        tmp[i]=0

tmp2=[0]*(n+1)
a=0
for i in range(1,n+1):
    a+=tmp[i]
    tmp2[i]=a

ans=[]
for x,y in q_lst:
    print(tmp2[y-1]-tmp2[x-1])
