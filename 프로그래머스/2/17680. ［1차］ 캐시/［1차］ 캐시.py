from collections import deque
def solution(cacheSize, cities):
    cache=deque(maxlen=cacheSize)
    time=0
    for i in cities:
        s=i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time+=1
        else:
            cache.append(s)
            time+=5
    return time
