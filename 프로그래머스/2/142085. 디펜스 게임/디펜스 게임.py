import heapq
def solution(n, k, enemy):
    answer = 0
    pq=enemy[:k]
    heapq.heapify(pq)
    for i in range(k,len(enemy)):
        heapq.heappush(pq,enemy[i])
        n-=heapq.heappop(pq)
        if n<0:
            return i
    return len(enemy)