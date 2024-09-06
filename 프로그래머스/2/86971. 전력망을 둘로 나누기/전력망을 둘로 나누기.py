from collections import deque


def bfs(n,graph):
    visit=[False]*(n+1)
    queue=deque()
    queue.append(1)
    visit[1]=True
    while queue:
        q=queue.popleft()
        for i in graph[q]:
            if not visit[i]:
                visit[i]=True
                queue.append(i)
    A=0
    B=0
    for i in range(1,len(visit)):
        if visit[i]==True:
            A+=1
        else:
            B+=1

    return abs(A-B)
    

            
    
def solution(n, wires):
    answer = 1e9
    graph=[[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer=min(answer,bfs(n,graph))
        
        graph[a].append(b)
        graph[b].append(a)
    
    return answer