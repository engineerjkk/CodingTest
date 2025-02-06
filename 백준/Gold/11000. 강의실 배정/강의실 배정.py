import sys 
input = sys.stdin.readline 
import heapq 

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
lst.sort()

rooms=[]
heapq.heappush(rooms,lst[0][1])
for i in range(1,n):
    if lst[i][0]<rooms[0]:
        heapq.heappush(rooms,lst[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms,lst[i][1])
print(len(rooms))