from collections import deque

N, M, R = map(int, input.split())

arr = []
new_arr = [[0]*M for _ in range(N)]
q = deque()

for i in range(N):
    arr.append(list(input().split()))

loops = min(N, M) // 2
for i in range(loops):
    q.clear()
    q.extend(arr[i][i:M-i])
    q.extend([row[M-i-1] for row in arr[i+1:N-i-1]])
    q.extend(arr[N-i-1][i:M-i][::-1])
    q.extend([row[i] for row in arr[i+1:N-i-1]][::-1])
    
    q.rotate(-R)
    
    for j in range(i, M-i):                 # 상
        new_arr[i][j] = q.popleft()
    for j in range(i+1, N-i-1):             # 우
        new_arr[j][M-i-1] = q.popleft()
    for j in range(M-i-1, i-1, -1):           # 하
        new_arr[N-i-1][j] = q.popleft()  
    for j in range(N-i-2, i, -1):           # 좌
        new_arr[j][i] = q.popleft()    

return new_arr