import sys
input = sys.stdin.readline
n,m=map(int,input().split())
lst=list(map(int,input().split()))
left=0
right=max(lst)
answer=0
while left<=right:
    mid=(left+right)//2
    tmp=[]
    for i in range(n):
        tmp.append(max(0,lst[i]-mid))
    if m<=sum(tmp):
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)