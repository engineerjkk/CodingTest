from collections import deque
def check(s):
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        else:
            if i==")" and stack[-1]=="(":
                stack.pop()
            elif i=="]" and stack[-1]=="[":
                stack.pop()
            elif i=="}" and stack[-1]=="{":
                stack.pop()
            else:
                stack.append(i)
    return len(stack)==0
        
def solution(s):
    answer=0
    n=len(s)
    queue=deque(s)
    for i in range(n):
        queue.rotate(-1)
        if check(queue):
            answer+=1
        
    return answer
        
        

                
    return answer