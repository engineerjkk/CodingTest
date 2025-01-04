import sys 
input = sys.stdin.readline 

n,k=map(int,input().split())
lst=list(map(int,input().split()))

lst.sort(reverse=True)
left=0
right=n-1

answer=0
while left<right:
    l=lst[left]
    r=lst[right]
    if l>=k:
        left+=1
        continue
    if l+r<=k:
        left+=1
        right-=1
        answer+=1
    if l+r>k:
        left+=1
print(answer)

