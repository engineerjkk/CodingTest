import sys
input = sys.stdin.readline

n,k=map(int,input().split())
a=list(map(int,input().split()))

low=max(a)
high=sum(a)
answer=-1

while low<=high:
    mid=(low+high)//2
    sum=0
    count=0
    for i in range(n):
        sum+=a[i]
        if sum>=mid:
            count+=1
            sum=0
    if count>=k:
        answer=mid
        low=mid+1
    else:
        high=mid-1
print(answer)