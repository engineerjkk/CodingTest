from collections import deque
def solution(n, edge):
    answer=0
    graph=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue=deque()
    queue.append(1)
    visited[1]=1
    while queue:
        q=queue.popleft()
        
        for i in graph[q]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=visited[q]+1
                
    for dis in visited:
        if dis ==max(visited):
            answer+=1
             
    return answer