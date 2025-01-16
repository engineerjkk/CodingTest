import sys 
input = sys.stdin.readline 
import heapq

left=[]
right=[]

n=int(input())
for _ in range(n):
    x=int(input())
    if len(left)==0 or -left[0]>=x:
        heapq.heappush(left,-x)
    else:
        heapq.heappush(right,x)
    
    if len(left)>len(right)+1:
        heapq.heappush(right,-heapq.heappop(left))
    elif len(right)>len(left):
        heapq.heappush(left,-heapq.heappop(right))
    
    print(-left[0])