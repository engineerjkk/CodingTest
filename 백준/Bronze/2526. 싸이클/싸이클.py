import sys
input = sys.stdin.readline
N,P=map(int,input().split())
n=N
dic={}
count=0
while True:
    n=n*N%P
    if n not in dic:
        dic[n]=count
        count+=1
    else:
        print(count-dic[n])
        break