from collections import deque
def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visit=[1e9]*(n+1)
    queue=deque()
    queue.append((1,0))
    tmp=0
    while queue:
        q,dis=queue.popleft()
        for i in graph[q]:
            if dis+1<visit[i]:
                visit[i]=dis+1
                queue.append((i,dis+1))
                tmp=max(tmp,dis+1)
    for i in range(2,len(visit)):
        if tmp==visit[i]:
            answer+=1
    return answer