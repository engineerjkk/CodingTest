import sys
input = sys.stdin.readline
n=int(input())
for i in range(n,-1,-1):
    tmp=str(i)
    flag=True
    for t in tmp:
        if t not in ['4','7']:
            flag=False
    if flag:
        print(i)
        exit()