arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

## zip
# 시계 방향 90 (= 반시계 방향 270)
arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)

# 시계 방향 180 (= 반시계 방향 180)
arr_180 = [a[::-1] for a in arr[::-1]]
print(arr_180)

# 시계 방향 270 (= 반시계 방향 90)
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
print(arr_270)