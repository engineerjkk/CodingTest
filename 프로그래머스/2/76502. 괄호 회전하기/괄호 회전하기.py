from collections import deque
def solution(s):
    
    def check(s):
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i=="}" and stack[-1]=="{":
                stack.pop()
            elif i=="]" and stack[-1]=="[":
                stack.pop()
            elif i==")" and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False
    
    n=len(s)
    queue=deque(s)
    answer=0
    for _ in range(n):
        if check(queue):
            answer+=1
        queue.rotate(-1)
    return answer
    

    
