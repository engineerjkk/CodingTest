import sys
import heapq

# 입력 받기 
n = int(sys.stdin.readline()) 
locations = []

# 집과 사무실 위치 입력받아 정렬하기
for _ in range(n):
   home, office = map(int, sys.stdin.readline().split())
   locations.append((min(home, office), max(home, office))) 
d = int(sys.stdin.readline())

# 끝점 기준 정렬
locations.sort(key=lambda x: x[1])

heap = []
max_people = 0

for location in locations:
   start, end = location
   heapq.heappush(heap, start)  # 시작점 저장
   rail_start = end - d  # 철로 시작점 = 현재 끝점 - 철로 길이
   
   # 철로 범위를 벗어나는 시작점 제거
   while heap and heap[0] < rail_start:
       heapq.heappop(heap)
       
   # 현재 철로에 포함된 사람 수 갱신
   max_people = max(max_people, len(heap))

print(max_people)