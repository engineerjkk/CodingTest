import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst=list(map(int,input().split()))
left=max(lst)
right=sum(lst)

while left<=right:
    mid=(left+right)//2
    remain=mid
    num=1
    for i in range(n):
        if remain<lst[i]:
            remain=mid
            num+=1
        remain-=lst[i]
    
    if num>m:
        left=mid+1
    else:
        right=mid-1
        answer=mid
print(answer)