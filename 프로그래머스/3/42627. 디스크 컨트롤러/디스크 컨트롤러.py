import heapq
def solution(jobs):
    answer,i,now=0,0,0
    start=-1
    pq=[]
    while i<len(jobs):
        for j in jobs:
            if start<j[0]<=now:
                heapq.heappush(pq,(j[1],j[0]))
        if pq:
            cur=heapq.heappop(pq)
            start=now
            now+=cur[0]
            answer+=now-cur[1]
            i+=1
        else:
            now+=1
    return answer//len(jobs)