from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    visit=[-1]*(n+1)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    queue=deque()
    queue.append(destination)
    visit[destination]=0
    while queue:
        q=queue.popleft()
        for i in graph[q]:
            if visit[i]==-1:
                queue.append(i)
                visit[i]=visit[q]+1
    for i in sources:
        answer.append(visit[i])
    return answer