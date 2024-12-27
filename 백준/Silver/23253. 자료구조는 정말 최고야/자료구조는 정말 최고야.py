import sys
input = sys.stdin.readline

n,m=map(int,input().split())

flag=True
for _ in range(m):
    k=int(input())
    book=list(map(int,input().split()))

    for i in range(1,len(book)):
        if book[i]>book[i-1]:
            flag=False
            break
if flag:
    print("Yes")
else:
    print("No")