import sys
input = sys.stdin.readline
import time
n,m = map(int,input().split())
lst=list(map(int,input().split()))

start=0
end=0
total=lst[0]
answer=0
while end<n:
    if total==m:
        answer+=1
    
    if total<m:
        end+=1
        if end==n:
            break
        total+=lst[end]
    else:
        total-=lst[start]
        start+=1
print(answer)
        
    
    