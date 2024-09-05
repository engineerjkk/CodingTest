def solution(arr1, arr2):
    n,m,r=len(arr1),len(arr1[0]),len(arr2[0])
    answer = [[0]*r for _ in range(n)]
    for i in range(n):
        for j in range(r):
            for k in range(m):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
    return answer