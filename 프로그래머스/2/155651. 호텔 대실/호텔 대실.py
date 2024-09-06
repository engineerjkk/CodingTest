import heapq
def solution(book_time):
    answer = 1
    book_ref=[]
    for s,e in book_time:
        s=int(s[:2])*60+int(s[3:])
        e=int(e[:2])*60+int(e[3:])
        book_ref.append([s,e])
    book_ref.sort()
    pq=[]
    for s,e in book_ref:
        if not pq:
            heapq.heappush(pq,e+10)
            continue
        if pq[0]<=s:
            heapq.heappop(pq)
        else:
            answer+=1
        heapq.heappush(pq,e+10)
    return answer