from heapq import heappush,heappop

def solution(operations):
    heap=[]
    for i in operations:
        op,num=i.split()
        num=int(num)
        if op=='I':
            heappush(heap,num)
        elif op=='D' and num== 1:
            if len(heap)!=0:
                a=max(heap)
                heap.remove(a)
        else:
            if len(heap)!=0:
                heappop(heap)
    if len(heap)==0:
        answer= [0,0]
    else:
        answer=[max(heap),heappop(heap)]
    return answer