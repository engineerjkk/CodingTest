import sys
input = sys.stdin.readline
n=int(input())
color=[]
for _ in range(n):
    color.append(list(map(int,input().split())))

R=[0]*n
G=[0]*n
B=[0]*n

R[0]=color[0][0]
G[0]=color[0][1]
B[0]=color[0][2]

for i in range(1,n):
    R[i]=color[i][0]+min(G[i-1],B[i-1])
    G[i]=color[i][1]+min(R[i-1],B[i-1])
    B[i]=color[i][2]+min(R[i-1],G[i-1])
print(min(R[-1],G[-1],B[-1]))