import sys 
input = sys.stdin.readline 

n=int(input())
scores=[]
for _ in range(n):
    scores.append(int(input()))

scores.sort()
answer=0
max_val=0
for i in reversed(range(n)):
    if scores[i]+n>=max_val:
        answer+=1
    else:
        break 
    max_val=max(max_val,scores[i]+n-i)
print(answer)