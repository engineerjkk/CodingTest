from collections import deque
def solution(queue1, queue2):
    q1=deque(queue1)
    q2=deque(queue2)
    sum1=sum(queue1)
    sum2=sum(queue2)
    limit=len(queue1)*3
    answer=0
    while sum1!=sum2:
        if sum1<sum2:
            num=q2.popleft()
            q1.append(num)
            sum2-=num
            sum1+=num
        elif sum2<sum1:
            num=q1.popleft()
            q2.append(num)
            sum1-=num
            sum2+=num
        answer+=1
        if answer==limit:
            return -1
            
    return answer