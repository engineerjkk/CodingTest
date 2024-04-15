import sys
input = sys.stdin.readline
n=int(input())
score=list(map(int,input().split()))
MAX=max(score)
new_score=[]
value=0
for i in score:
    value+=(i/MAX)

print((value/n)*100)

