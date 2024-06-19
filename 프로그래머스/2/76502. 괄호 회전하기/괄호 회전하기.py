from collections import deque

def check(s):
    stack=[]
    for q in s:
        if len(stack)==0:
            stack.append(q)
        elif q=="}" and stack[-1]=="{":
            stack.pop()
        elif q=="]" and stack[-1]=="[":
            stack.pop()
        elif q==")" and stack[-1]=="(":
            stack.pop()
        else:
            stack.append(q)
    if len(stack)==0:
        return True
    else:
        return False

def solution(s):
    n=len(s)
    queue=deque(s)
    ans=0
    for _ in range(n):
        if check(queue):
            ans+=1
        queue.rotate(-1)
    return ans