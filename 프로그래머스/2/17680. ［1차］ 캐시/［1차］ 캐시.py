from collections import deque
def solution(cacheSize, cities):
    queue=deque(maxlen=cacheSize)
    time=0
    for i in cities:
        s=i.lower()
        if s in queue:
            queue.remove(s)
            queue.append(s)
            time+=1
        else:
            queue.append(s)
            time+=5
    return time
