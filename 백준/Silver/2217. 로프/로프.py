import sys
input = sys.stdin.readline
n=int(input())
w=[0]*n
for i in range(n):
    w[i]=int(input())

w.sort(reverse=True)
max_weight=0
for i in range(n):
    max_weight=max(max_weight,w[i]*(i+1))
print(max_weight)