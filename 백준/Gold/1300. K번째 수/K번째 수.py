import sys
input = sys.stdin.readline

def Count(x,n):
    count=0
    for i in range(1,n+1):
        count+=min(x//i,n)
    return count

def solution(n,k):
    left,right=1,k
    while left<=right:
        mid=(left+right)//2
        count=Count(mid,n)

        if count<k:
            left=mid+1
        else:
            answer=mid
            right=mid-1
    return answer

        

n=int(input())
k=int(input())
print(solution(n,k))