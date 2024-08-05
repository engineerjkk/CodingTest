import sys
input = sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
psum=[0]*n
psum[0]=a[0]
for i in range(1,n):
    psum[i]=psum[i-1]+a[i]

answer=0
count={}
for i in range(n):
    goal=psum[i]-k

    if goal==0:
        answer+=1
    if goal in count:
        answer+=count[goal]
    if psum[i] not in count:
        count[psum[i]]=0
    count[psum[i]]+=1
print(answer)
