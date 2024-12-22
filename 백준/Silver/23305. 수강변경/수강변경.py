import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dic={}
for i in range(n):
    if a[i] not in dic:
        dic[a[i]]=[0,0]
    dic[a[i]][0]+=1

    if b[i] not in dic:
        dic[b[i]]=[0,0]
    dic[b[i]][1]+=1

cnt=0
for key,value in dic.items():
    supply=value[0]
    demand=value[1]
    cnt+=min(supply,demand)
print(n-cnt)