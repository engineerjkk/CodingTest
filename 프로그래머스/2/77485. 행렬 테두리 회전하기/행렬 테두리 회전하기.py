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
        for r in range(c1,c2+1):
            queue.append(space[r1][r])
        for c in range(r1+1,r2):
            queue.append(space[c][c2])
        for r in range(c1,c2+1)[::-1]:
            queue.append(space[r2][r])
        for c in range(r1+1,r2)[::-1]:
            queue.append(space[c][c1])
        
        queue.rotate(1)
        answer.append(min(queue))

        for r in range(c1,c2+1):
            space[r1][r]=queue.popleft()
        for c in range(r1+1,r2):
            space[c][c2]=queue.popleft()
        for r in range(c1,c2+1)[::-1]:
            space[r2][r]=queue.popleft()
        for c in range(r1+1,r2)[::-1]:
            space[c][c1]=queue.popleft()

    return answer