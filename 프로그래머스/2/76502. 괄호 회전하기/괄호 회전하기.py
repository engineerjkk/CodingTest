from collections import deque

def check(s):
    stack=[]
    n=len(s)
    for i in range(n):
        if len(stack)==0:
            stack.append(s[i])
        else:
            if stack[-1]=='[' and s[i]==']':
                stack.pop()
            elif stack[-1]=='(' and s[i]==')':
                stack.pop()
            elif stack[-1]=='{' and s[i]=='}':
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack)==0:
        return True
    else:
        return False
            

def solution(s):
    answer = 0
    n=len(s)
    s=deque(s)
    while n:
        if check(s):
            answer+=1
        s.rotate(1)
        n-=1
    return answer