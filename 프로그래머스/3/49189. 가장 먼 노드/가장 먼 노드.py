from collections import deque
def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    visit=[-1]*(n+1)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue=deque()
    queue.append(1)
    visit[1]=0
    while queue:
        q=queue.popleft()
        for i in graph[q]:
            if visit[i]==-1:
                visit[i]=visit[q]+1
                queue.append(i)
    for i in range(len(visit)):
        if visit[i]==max(visit):
            answer+=1
    return answer