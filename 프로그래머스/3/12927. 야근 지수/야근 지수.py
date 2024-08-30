import heapq
def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return answer
    else:
        wrk=[]
        for i in works:
            wrk.append(-i)
        heapq.heapify(wrk)
        while n:
            heapq.heappush(wrk,heapq.heappop(wrk)+1)
            n-=1
        for i in wrk:
            answer+=i**2
        
    return answer