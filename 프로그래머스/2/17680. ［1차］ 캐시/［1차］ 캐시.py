from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue=deque(maxlen=cacheSize)
    time=0
    for city in cities:
        city=city.lower()
        if city in queue:
            queue.remove(city)
            queue.append(city)
            time+=1
        else:
            queue.append(city)
            time+=5
    return time