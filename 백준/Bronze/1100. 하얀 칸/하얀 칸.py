import sys
input = sys.stdin.readline

space=[]
for _ in range(8):
    space.append(list(input().strip()))

flag=True
flag_col=True
cnt=0
for i in range(8):
    for j in range(8):
        if space[i][j]=='F' and flag:
            cnt+=1
        if flag:
            flag=False
        else:
            flag=True
    if flag:
        flag=False
    else:
        flag=True
print(cnt)