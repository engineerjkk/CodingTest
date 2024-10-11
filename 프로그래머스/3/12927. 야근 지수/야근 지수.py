import heapq
def solution(n, works):
    if sum(works)<=n:
        return 0
    pq=[]
    for i in range(len(works)):
        heapq.heappush(pq,-works[i])
    
    while n:
        heapq.heappush(pq,heapq.heappop(pq)+1)
        n-=1
    answer=0
    while pq:
        answer+=heapq.heappop(pq)**2
    return answer