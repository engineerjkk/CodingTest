import sys 
input = sys.stdin.readline 
n=int(input())
cranes=list(map(int,input().split()))
m=int(input())
boxes=list(map(int,input().split()))

time=0
cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0]<boxes[0]:
    print(-1)
    exit()

while boxes:
    time+=1
    idx=0
    for crane in cranes:
        if len(boxes)==0:
            break 
        while idx<len(boxes):
            if boxes[idx]<=crane:
                boxes.pop(idx)
                break
            idx+=1
print(time)