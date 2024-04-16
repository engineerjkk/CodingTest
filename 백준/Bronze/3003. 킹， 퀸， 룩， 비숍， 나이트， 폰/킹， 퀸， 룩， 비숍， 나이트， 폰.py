import sys
input=sys.stdin.readline

#16개, king=1,queen=1, look=2, bishop=2,night=2,phone=8
chess=[1,1,2,2,2,8]
dong=list(map(int,input().split()))
for i,j in zip(chess,dong):
    print(i-j,end=" ")

