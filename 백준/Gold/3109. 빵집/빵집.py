import sys 
input = sys.stdin.readline 

n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(str,input().strip())))
visit=[[False]*m for _ in range(n)]

def dfs(r,c):
    visit[r][c]=True 
    if c==m-1:
        return True 
    if r-1>=0 and not visit[r-1][c+1] and space[r-1][c+1]=='.':
        if dfs(r-1,c+1):
            return True
    if not visit[r][c+1] and space[r][c+1]=='.':
        if dfs(r,c+1):
            return True 
    
    if r+1<n and not visit[r+1][c+1] and space[r+1][c+1]=='.':
        if dfs(r+1,c+1):
            return True 
    return False

answer=0
for i in range(n):
    if dfs(i,0):
        answer+=1
print(answer)