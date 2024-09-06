import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
m=int(input())
left=0
right=max(lst)
while left<=right:
    mid=(left+right)//2
    tmp=0
    for i in lst:
        tmp+=min(i,mid)
    if tmp<=m:
        left=mid+1
        answer=mid
    else:
        right=mid-1
print(answer)