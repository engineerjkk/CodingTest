from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    visit=[-1]*(n+1)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    visit[destination]=0
    queue=deque()
    queue.append((destination,0))
    tmp=0
    while queue:
        q,dis=queue.popleft()
        for i in graph[q]:
            if visit[i]==-1:
                visit[i]=dis+1
                queue.append((i,dis+1))
                tmp=max(tmp,dis+1)
    answer=[]
    for i in sources:
        answer.append(visit[i])
    return answer