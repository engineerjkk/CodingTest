from collections import deque

def solution(rows, columns, queries):
    board, i = [], 1
    for row in range(rows):
        board.append(list(range(i, i + columns)))
        i += columns

    answer, queue = [], deque()
    for query in queries:
        r1, c1, r2, c2 = query
        r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

        # 위쪽 라인 처리
        for cr in range(c1, c2 + 1):
            queue.append(board[r1][cr])
        # 오른쪽 라인 처리
        for cc in range(r1 + 1, r2):
            queue.append(board[cc][c2])
        # 아래쪽 라인 처리
        for cr in range(c1, c2 + 1)[::-1]:
            queue.append(board[r2][cr])
        # 왼쪽 라인 처리
        for cc in range(r1 + 1, r2)[::-1]:
            queue.append(board[cc][c1])

        answer.append(min(queue))
        queue.rotate(1)

        # 큐에서 값을 빼면서 다시 보드에 값 채워넣기
        for cr in range(c1, c2 + 1):
            board[r1][cr] = queue.popleft()
        for cc in range(r1 + 1, r2):
            board[cc][c2] = queue.popleft()
        for cr in range(c1, c2 + 1)[::-1]:
            board[r2][cr] = queue.popleft()
        for cc in range(r1 + 1, r2)[::-1]:
            board[cc][c1] = queue.popleft()

    return answer
