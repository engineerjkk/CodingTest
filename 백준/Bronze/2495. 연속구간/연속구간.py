import sys
input = sys.stdin.readline

answer=[]
for _ in range(3):
    num=list(map(str,input().strip()))
    cnt=0
    MAX=0
    for i in range(7):
        if num[i+1]==num[i]:
            cnt+=1
            MAX=max(MAX,cnt)
        else:
            cnt=0
    answer.append(MAX)
for i in answer:
    if i==0:
        print(1)
    else:
        print(i+1)