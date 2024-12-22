import sys
input = sys.stdin.readline

n=int(input())
cranes=list(map(int,input().split()))
m=int(input())
boxes=list(map(int,input().split()))

def solution(n,cranes,m,boxes):
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)
    time=0

    if cranes[0]<boxes[0]:
        return -1
    
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
    return time
        

print(solution(n,cranes,m,boxes))