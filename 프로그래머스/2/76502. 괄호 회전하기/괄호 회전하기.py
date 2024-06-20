from collections import deque
def solution(s):
    
    def check(s):
        stack=[]
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i]=="}" and stack[-1]=="{":
                stack.pop()
            elif s[i]=="]" and stack[-1]=="[":
                stack.pop()
            elif s[i]==")" and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack)==0:
            return True
        else:
            return False
    answer=0
    n=len(s)
    queue=deque(s)
    for _ in range(n):
        if check(queue):
            answer+=1
        queue.rotate(-1)
    return answer
    
    
    
