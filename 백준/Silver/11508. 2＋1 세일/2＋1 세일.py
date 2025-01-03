import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
answer=0
cnt=0
while lst:
    answer+=lst.pop(0)
    cnt+=1
    if lst and cnt==2:
        lst.pop(0)
        cnt=0
print(answer)