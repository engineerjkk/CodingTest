import sys
input = sys.stdin.readline
import heapq

n=int(input())
locations=[]
for _ in range(n):
    home,office=map(int,input().split())
    locations.append((min(home,office),max(home,office)))

d=int(input())

locations.sort(key=lambda x:x[1])

max_people=0
pq=[]
for start,end in locations:
    heapq.heappush(pq,start)
    start_rail=end-d

    while pq and pq[0]<start_rail:
        heapq.heappop(pq)
    
    max_people=max(max_people,len(pq))

print(max_people)