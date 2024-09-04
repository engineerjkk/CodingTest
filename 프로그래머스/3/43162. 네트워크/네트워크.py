from collections import deque
def solution(n, computers):
    answer = 0
    visit=[False]*n
    
    def bfs(start,visit,computers):
        queue=deque()
        queue.append(start)
        visit[start]=True
        while queue:
            q=queue.popleft()
            for i in range(len(computers[q])):
                if not visit[i] and computers[q][i]==1:
                    visit[i]=True
                    queue.append(i)
    
    for i in range(n):
        if not visit[i]:
            bfs(i,visit,computers)
            answer+=1
    return answer