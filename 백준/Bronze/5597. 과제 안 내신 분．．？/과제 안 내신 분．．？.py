import sys
input = sys.stdin.readline
lst=[]
for _ in range(28):
    lst.append(int(input()))

arr=[0]*31

for i in lst:
    arr[i]+=1

for i in range(1,31):
    if arr[i]==0:
        print(i)
