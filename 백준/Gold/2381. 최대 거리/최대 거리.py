import sys 
input = sys.stdin.readline

n=int(input())
sum_xy=[]
diff_xy=[]
for _ in range(n):
    x,y=map(int,input().split())
    sum_xy.append(x+y)
    diff_xy.append(x-y)

answer=max(
    (max(sum_xy)-min(sum_xy)),
    (max(diff_xy)-min(diff_xy)))
print(answer)