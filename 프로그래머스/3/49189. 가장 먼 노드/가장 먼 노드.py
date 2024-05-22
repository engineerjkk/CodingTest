from collections import deque
def solution(n, edge):
    answer=0
    graph=[[] for _ in range(n+1)]
    distance=[-1]*(n+1)
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue=deque()
    queue.append(1)
    distance[1]=0
    
    while queue:
        q=queue.popleft()
        for i in graph[q]:
            if distance[i]==-1:
                queue.append(i)
                distance[i]=distance[q]+1
    
    for i in distance:
        if i==max(distance):
            answer+=1
    
             
    return answer