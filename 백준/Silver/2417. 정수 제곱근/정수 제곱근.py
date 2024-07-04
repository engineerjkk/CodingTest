import sys
input = sys.stdin.readline
n=int(input())
left=0
right=2**63
answer=0
while left<=right:
    mid=(left+right)//2

    if mid**2<n:
        left=mid+1
    else:
        answer=mid
        right=mid-1
print(answer)