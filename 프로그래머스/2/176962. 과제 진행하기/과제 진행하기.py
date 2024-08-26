from collections import deque
def solution(plans):
    answer = []
    lst=[]
    for plan in plans:
        name,start,playtime=plan
        start=int(start[:2])*60+int(start[3:])
        playtime=int(playtime)
        lst.append([name,start,playtime])
    lst.sort(key=lambda x:x[1])
    queue=deque(lst)
    lst=[]
    while queue:
        name,start,playtime=queue.popleft()
        for i,v in enumerate(lst):
            if start<v[0]:
                lst[i][0]+=playtime
        lst.append([start+playtime,name])
    lst.sort(key=lambda x:x[0])
    for t,n in lst:
        answer.append(n)
        
    return answer