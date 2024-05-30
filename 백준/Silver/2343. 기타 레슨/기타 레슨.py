import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst=list(map(int,input().split()))

left=max(lst)
right=sum(lst)

while left<=right:
    mid=(left+right)//2
    total=0

    num=1
    remain=mid
    for i in range(n):
        if remain<lst[i]:
            num+=1
            remain=mid
        remain-=lst[i]
    if num<=m:
        right=mid-1
        answer=mid
    else:
        left=mid+1  
print(answer)

