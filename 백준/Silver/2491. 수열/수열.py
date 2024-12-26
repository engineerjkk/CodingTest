import sys
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

flag=False
answer_up=0
answer_down=0
cnt_down=0
cnt_up=0
for i in range(n-1):
    if lst[i+1]<=lst[i]:
        cnt_down+=1
    else:
        cnt_down=0
    
    if lst[i+1]>=lst[i]:
        cnt_up+=1
    else:
        cnt_up=0
    answer_down=max(answer_down,cnt_down)
    answer_up=max(answer_up,cnt_up)
print(max(answer_up,answer_down)+1) 
