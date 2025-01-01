import sys
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
x=int(input())

count=[0]*1000001
for i in range(n):
    count[lst[i]]+=1

answer=0
for i in range((x+1)//2):
    if x-i>=1000000:
        continue
    answer+=count[i]*count[x-i]

if x%2==0:
    answer+=count[x//2]*(count[x//2]-1)//2
print(answer)