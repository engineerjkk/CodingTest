import heapq
def solution(n, works):
    answer = 0
    tmp=[]
    if sum(works)<=n:
        return 0
    for i in range(len(works)):
        tmp.append(-works[i])
    heapq.heapify(tmp)
    for _ in range(n):
        heapq.heappush(tmp,heapq.heappop(tmp)+1)
    while tmp:
        answer+=heapq.heappop(tmp)**2
    return answer