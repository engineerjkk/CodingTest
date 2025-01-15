import sys 
input = sys.stdin.readline 
import copy

N = int(input())
scores = [int(input()) for _ in range(N)]

scores.sort()

answer=0
max_val=0
for i in reversed(range(N)):
    if scores[i]+N>=max_val:
        answer+=1 
    else:
        break 
    max_val=max(max_val,scores[i]+N-i)
print(answer)


