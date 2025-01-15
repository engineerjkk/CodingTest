import sys 
input = sys.stdin.readline 

n=int(input())
distance=[]
for _ in range(n):
    distance.append(list(map(int,input().split())))
needs=[[True]*n for _ in range(n)]

impossible=False
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==j or j==k:
                continue 
            if distance[i][j]+distance[j][k]==distance[i][k]:
                needs[i][k]=False
            if distance[i][j]+distance[j][k]<distance[i][k]:
                impossible=True
                break 

if impossible:
    print(-1)
else:
    answer=0
    for i in range(n):
        for j in range(i,n):
            if needs[i][j]:
                answer+=distance[i][j]
    print(answer)