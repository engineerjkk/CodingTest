import sys
input = sys.stdin.readline 
import heapq

n = int(input())
left = []   # 중간값을 포함한 이전 값 최대힙
right = []  # 중간값 이후의 값 최소힙

for i in range(n):
    x = int(input())

    if len(left) == 0 or -left[0] >= x:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    if len(left) > len(right) + 1:
        temp = -heapq.heappop(left)
        heapq.heappush(right, temp)
    elif len(right) > len(left):
        temp = heapq.heappop(right)
        heapq.heappush(left, -temp)

    print(-left[0])