from collections import deque
def solution(plans):
    answer = []
    queue=deque()
    lst=[]
    for plan in plans:
        study,start,playtime=plan
        start=int(start[:2])*60+int(start[3:])
        playtime=int(playtime)
        lst.append((study,start,playtime))
    lst.sort(key=lambda x:x[1])
    queue=deque(lst)
    lst=[]
    while queue:
        study,start,playtime=queue.popleft()
        for i in range(len(lst)):
            n,t=lst[i]
            if start<t:
                lst[i][1]+=playtime
        lst.append([study,start+playtime])
    lst.sort(key=lambda x:x[1])
    for n,t in lst:
        answer.append(n)
    return answer