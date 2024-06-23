from collections import deque
def solution(cacheSize, cities):
    queue=deque(maxlen=cacheSize)
    time=0
    for i in cities:
        i=i.lower()
        if i in queue:
            queue.remove(i)
            queue.append(i)
            time+=1
        else:
            queue.append(i)
            time+=5
    return time
        

