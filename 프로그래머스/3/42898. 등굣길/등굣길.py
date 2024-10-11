def solution(m, n, puddles):
    space=[[0]*(m+1) for _ in range(n+1)]
    space[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            elif [j,i] in puddles:
                space[i][j]=0
            else:
                space[i][j]=space[i-1][j]+space[i][j-1]
    return space[n][m]%1000000007