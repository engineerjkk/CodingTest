import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
limit=int(input())

left=0
right=max(lst)
answer=0
while left<=right:
    mid=(left+right)//2
    total=0
    for i in lst:
        total+=min(mid,i)
    if total<=limit:
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)