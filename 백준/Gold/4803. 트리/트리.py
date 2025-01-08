import sys 
input = sys.stdin.readline 
from collections import deque 

test_case=1
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break 
    graph=[[] for _ in range(n)]
    for _ in range(m):
        u,v=map(int,input().split())
        u-=1
        v-=1
        graph[u].append(v)
        graph[v].append(u)
    
    visit=[False]*n
    queue=deque()
    num_trees=0
    for i in range(n):
        if not visit[i]:
            queue.append(i)
            visit[i]=True 

            num_nodes=1
            num_edges=0

            while queue:
                u=queue.popleft()
                for v in graph[u]:
                    num_edges+=1
                    if not visit[v]:
                        queue.append(v)
                        visit[v]=True 
                        num_nodes+=1 

            num_edges//=2
            if num_edges==num_nodes-1:
                num_trees+=1 
    
    if num_trees == 0:
        print(f"Case {test_case}: No trees.")
    elif num_trees == 1:
        print(f"Case {test_case}: There is one tree.")
    else:
        print(f"Case {test_case}: A forest of {num_trees} trees.")
    test_case += 1