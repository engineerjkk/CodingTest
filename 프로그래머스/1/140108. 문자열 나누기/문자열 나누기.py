from collections import deque
def solution(s):
    answer = 1
    queue=[]
    queue.append(s[0])
    cnt=0
    for i in s[1:]:
        if len(queue)==0:
            answer+=1
            queue.append(i)
        else:
            q=queue.pop()
            if q==i:
                queue.append(q)
                queue.append(i)
            else:
                continue
        
    return answer+cnt