import heapq
def solution(book_time):
    answer = 1
    book_time_ref=[]
    for s,e in book_time:
        start=int(s[:2])*60+int(s[3:])
        end=int(e[:2])*60+int(e[3:])
        book_time_ref.append((start,end))
    book_time_ref.sort()
    
    heap=[]
    for s,e in book_time_ref:
        if not heap:
            heapq.heappush(heap,e+10)
            continue
        if heap[0]<=s:
            heapq.heappop(heap)
        else:
            answer+=1
        heapq.heappush(heap,e+10)
        
    return answer