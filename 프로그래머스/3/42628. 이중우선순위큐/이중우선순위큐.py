import heapq
def solution(operations):
    answer = []
    pq=[]
    heapq.heapify(pq)
    for operation in operations:
        op,num=operation.split()
        if op=='I':
            heapq.heappush(pq,int(num))
        elif op=='D' and num=='1':
            if pq:
                pq.remove(max(pq))
        else:
            if pq:
                heapq.heappop(pq)
    if not pq:
        return [0,0]
    else:
        return [max(pq),heapq.heappop(pq)]
            
