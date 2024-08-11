from collections import deque
def solution(n, wires):
    res=0
    graph=[[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visit=[False]*(n+1)
        queue=deque()
        queue.append(start)
        visit[start]=True
        cnt=1
        while queue:
            q=queue.popleft()
            for i in graph[q]:
                if not visit[i]:
                    queue.append(i)
                    visit[i]=True
                    cnt+=1
        return cnt
    
    res = n 
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        res=min(abs(bfs(a)-bfs(b)),res)
        graph[a].append(b)
        graph[b].append(a)
        
    return res