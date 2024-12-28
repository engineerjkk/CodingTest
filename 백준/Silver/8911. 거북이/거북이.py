import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]  # 북, 동, 남, 서
dc = [0, 1, 0, -1]

class Player:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
    def go(self):
        self.r += dr[self.d]
        self.c += dc[self.d]
    def back(self):
        self.r -= dr[self.d]
        self.c -= dc[self.d]
    def left(self):
        self.d = (self.d + 3) % 4
    def right(self):
        self.d = (self.d + 1) % 4

t = int(input())
for _ in range(t):
    orders = input().strip()
    
    # 시작 위치를 (0,0)으로 설정하고 북쪽을 바라보도록 초기화
    player = Player(0, 0, 0)
    
    # 거북이가 지나간 모든 좌표를 저장
    visited = [(0, 0)]
    
    # 명령 실행
    for order in orders:
        if order == 'F':
            player.go()
        elif order == 'B':
            player.back()
        elif order == 'L':
            player.left()
        else:  # R
            player.right()
        visited.append((player.r, player.c))
    
    # 최소/최대 좌표 찾기
    min_r = min(v[0] for v in visited)
    max_r = max(v[0] for v in visited)
    min_c = min(v[1] for v in visited)
    max_c = max(v[1] for v in visited)
    
    # 직사각형 넓이 계산
    width = max_c - min_c
    height = max_r - min_r
    area = width * height
    
    print(area)