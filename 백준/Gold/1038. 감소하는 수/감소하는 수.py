import sys 
input = sys.stdin.readline 
from itertools import combinations 

n=int(input())
answer=[]
for i in range(1,11):
    for nCr in combinations(list(reversed(range(10))),i):
        tmp=""
        for j in nCr:
            tmp+=str(j)
        answer.append(int(tmp))
answer.sort()
if len(answer)<=n:
    print(-1)
else:
    print(answer[n])
        