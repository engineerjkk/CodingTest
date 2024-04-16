## 인덱싱
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3
# 시계 방향 90 (= 반시계 방향 270)
new_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_90[j][n - i - 1] = arr[i][j]
print(new_90)

# 시계 180 & 반시계 180
new_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_180[n - i - 1][n - j - 1] = arr[i][j]
print(new_180)

# 시계 270 & 반시계 90
new_270 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_270[n - 1 - j][i] = arr[i][j]
print(new_270)