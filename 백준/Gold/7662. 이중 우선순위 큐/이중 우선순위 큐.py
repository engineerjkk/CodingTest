import sys 
input = sys.stdin.readline 
import heapq 

t=int(input())
for _ in range(t):
    k=int(input())
    max_pq=[]
    min_pq=[]
    count={}
    for _ in range(k):
        cmd,num=input().split()
        num=int(num)

        if cmd=='I':
            heapq.heappush(max_pq,-num)
            heapq.heappush(min_pq,num)

            if num not in count:
                count[num]=1
            else:
                count[num]+=1
        else:
            if count:
                if num==1:
                    while max_pq and -max_pq[0] not in count:
                        heapq.heappop(max_pq)
                    if max_pq:
                        max_num = -heapq.heappop(max_pq)
                        count[max_num]-=1
                        if count[max_num]==0:
                            del count[max_num]
                else:
                    while min_pq and min_pq[0] not in count:
                        heapq.heappop(min_pq)
                    if min_pq:
                        min_num = heapq.heappop(min_pq)
                        count[min_num]-=1
                        if count[min_num]==0:
                            del count[min_num]    
    while max_pq and -max_pq[0] not in count:  
        heapq.heappop(max_pq)    
    while min_pq and min_pq[0] not in count:
        heapq.heappop(min_pq)
    
    if not max_pq or not min_pq:
        print("EMPTY")
    else:
        print(-max_pq[0],min_pq[0])
