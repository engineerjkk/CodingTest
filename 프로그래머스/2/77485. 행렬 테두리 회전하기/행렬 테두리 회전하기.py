from collections import deque
def solution(rows, columns, queries):
    answer = []
    space=[[0]*columns for _ in range(rows)]
    cnt=1
    for i in range(rows):
        for j in range(columns):
            space[i][j]=cnt
            cnt+=1
    for query in queries:
        r1,c1,r2,c2=query
        r1,c1,r2,c2=r1-1,c1-1,r2-1,c2-1
        queue=deque()
        for cr in range(c1,c2+1):
            queue.append(space[r1][cr])
        for cc in range(r1+1,r2):
            queue.append(space[cc][c2])
        for cr in range(c1,c2+1)[::-1]:
            queue.append(space[r2][cr])
        for cc in range(r1+1,r2)[::-1]:
            queue.append(space[cc][c1])
        
        queue.rotate(1)
        answer.append(min(queue))
        
        for cr in range(c1,c2+1):
            space[r1][cr]=queue.popleft()
        for cc in range(r1+1,r2):
            space[cc][c2]=queue.popleft()
        for cr in range(c1,c2+1)[::-1]:
            space[r2][cr]=queue.popleft()
        for cc in range(r1+1,r2)[::-1]:
            space[cc][c1]=queue.popleft()
    
    return answer