import sys
input = sys.stdin.readline
from collections import deque

def get_password(alpha):
    left=deque()
    right=deque()

    for key in alpha:
        if key=='<':
            if left:
                right.appendleft(left.pop())
        elif key=='>':
            if right:
                left.append(right.popleft())
        elif key=='-':
            if left:
                left.pop()
        else:
            left.append(key)
    return ''.join(left)+''.join(right)

t=int(input())
for _ in range(t):
    alpha=input().strip()
    password=get_password(alpha)
    print(password)