import sys
input = sys.stdin.readline
n = int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

end=lst[-1]
cnt=0
for i in range(n-2,-1,-1):
    if lst[i]>=end:
        cnt+=(lst[i]-end+1)
        lst[i]-=(lst[i]-end+1)
        end=lst[i]
    else:
        end=lst[i]
print(cnt)
