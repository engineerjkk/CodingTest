import sys
input = sys.stdin.readline

n,a,b=map(int,input().split())
answer=0
while a!=b:
    a=(a+1)//2
    b=(b+1)//2
    answer+=1
print(answer)