from collections import deque
def solution(n, wires):
    answer=n
    graph=[[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        cnt=0
        queue=deque()
        queue.append(start)
        visit=[False]*(n+1)
        visit[start]=True
        while queue:
            q=queue.popleft()
            for i in graph[q]:
                if not visit[i]:
                    visit[i]=True
                    queue.append(i)
                    cnt+=1
        return cnt
    
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer=min(answer,abs(bfs(a)-bfs(b)))
        graph[a].append(b)
        graph[b].append(a)
        
    return answer