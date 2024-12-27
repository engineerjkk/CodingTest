import sys
input = sys.stdin.readline
from collections import deque

n = int(input())  # 도시의 수
m = int(input())  # 여행 계획에 속한 도시의 수

# 도시간 연결 정보 입력
space = []
for i in range(n):
    space.append(list(map(int, input().split())))

# 여행 계획 입력
path = list(map(int, input().split()))

# 경로 가능 여부 확인
def bfs(start, target):
    queue = deque([start-1])  # 0-based 인덱스로 변환
    visited = [False] * n
    visited[start-1] = True
    
    while queue:
        current = queue.popleft()
        if current == target-1:  # 목표 도시 도달
            return True
            
        for next_city in range(n):
            if space[current][next_city] == 1 and not visited[next_city]:
                queue.append(next_city)
                visited[next_city] = True
                
    return False

# 연속된 도시들이 연결되어 있는지 확인
possible = True
for i in range(m-1):
    if not bfs(path[i], path[i+1]):
        possible = False
        break

print("YES" if possible else "NO")