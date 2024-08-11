def solution(order):
    i=1
    idx=0
    n=len(order)
    stack=[]
    while i<n+1:
        stack.append(i)
        while stack[-1]==order[idx]:
            stack.pop()
            idx+=1
            if len(stack)==0:
                break
        i+=1
    return idx