from collections import deque
import sys
input = sys.stdin.readline
n=int(input())
queue=deque()
answer=[]
for _ in range(n):
    order=input().split()
    if len(order)==1:
        order=order[0]
    else:
        order,num=order[0],int(order[1])
    
    if order=="pop":
        if len(queue)>0:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif order=="size":
        answer.append(len(queue))
    elif order=="empty":
        if len(queue)==0:
            answer.append(1)
        else:
            answer.append(0)
    elif order=="front":
        if len(queue)>0:
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif order=="back":
        if len(queue)>0:
            answer.append(queue[-1])
        else:
            answer.append(-1)
    else:
        num=int(num)
        queue.append(num)
for i in answer:
    print(i)    